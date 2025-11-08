"""Razorpay client."""

# Standard library imports
import json
import logging
import os
import random
import time
import warnings
from importlib.metadata import PackageNotFoundError, version
from types import ModuleType

# Other third-party library imports
import requests

# Razorpay SDK local imports
from . import resources, utility
from .constants import ERROR_CODE, URL, HttpStatusCode
from .errors import BadRequestError, GatewayError, ServerError


def capitalize_camel_case(string):
    """Convert a snake_case string to CamelCase."""
    return "".join(map(str.capitalize, string.split("_")))


# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and capitalize_camel_case(name) in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[capitalize_camel_case(name)]

UTILITY_CLASSES = {}
for name, module in utility.__dict__.items():
    if isinstance(module, ModuleType) and name.capitalize() in module.__dict__:
        UTILITY_CLASSES[name] = module.__dict__[name.capitalize()]

DEFAULT_RETRY_OPTIONS = {
    "base_url": URL.BASE_URL,
    "max_retries": 5,
    "initial_delay": 1,
    "max_delay": 60,
    "jitter": 0.25,
}

logger = logging.getLogger(__name__)


class Client:
    """Razorpay client class."""

    def __init__(self, session=None, auth=None, **options):
        self.session = session or requests.Session()
        self.auth = auth
        file_dir = os.path.dirname(__file__)
        self.cert_path = file_dir + "/ca-bundle.crt"

        self.base_url = self._set_base_url(**options)
        self.max_retries = options.get("max_retries", DEFAULT_RETRY_OPTIONS["max_retries"])
        self.initial_delay = options.get("initial_delay", DEFAULT_RETRY_OPTIONS["initial_delay"])
        self.max_delay = options.get("max_delay", DEFAULT_RETRY_OPTIONS["max_delay"])
        self.jitter = options.get("jitter", DEFAULT_RETRY_OPTIONS["jitter"])
        self.retry_enabled = False

        self.app_details = []

        # intializes each resource
        # injecting this client object into the constructor
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

        for name, Klass in UTILITY_CLASSES.items():
            setattr(self, name, Klass(self))

    def _set_base_url(self, **options):
        base_url = DEFAULT_RETRY_OPTIONS["base_url"]

        if "base_url" in options:
            base_url = options["base_url"]
            del options["base_url"]

        # Remove retry options from options if they exist
        options.pop("max_retries", None)
        options.pop("initial_delay", None)
        options.pop("max_delay", None)
        options.pop("jitter", None)

        return base_url

    def _update_user_agent_header(self, options):
        user_agent = "{}{} {}".format(
            "Razorpay-Python/", self._get_version(), self._get_app_details_ua()
        )

        if "headers" in options:
            options["headers"]["User-Agent"] = user_agent
        else:
            options["headers"] = {"User-Agent": user_agent}

        return options

    def _get_version(self):
        try:
            return version("razorpay-py")
        except (PackageNotFoundError, NameError):
            # If all else fails, use the hardcoded version from the package

            warnings.warn(
                "Could not detect razorpay package version. Using fallback version."
                "This may indicate an installation issue.",
                UserWarning,
                stacklevel=4,
            )
            return "1.4.3"

    def _get_app_details_ua(self):
        app_details_ua = ""

        app_details = self.get_app_details()

        for app in app_details:
            if "title" in app:
                app_ua = app["title"]
                if "version" in app:
                    app_ua += "/{}".format(app["version"])
                app_details_ua += f"{app_ua} "

        return app_details_ua

    def set_app_details(self, app_details):
        """Add an app detail entry to be included in the User-Agent header.

        Args:
            app_details (dict): A dictionary with optional 'title' and 'version'
                keys describing the application using the SDK.
        """
        self.app_details.append(app_details)

    def get_app_details(self):
        """Retrieve all app details added via `set_app_details`.

        Returns:
            list: A list of dictionaries representing app details.
        """
        return self.app_details

    def enable_retry(self, retry_enabled=False):
        """Enable/disable retry strategy."""
        self.retry_enabled = retry_enabled

    def request(self, method, path, **options):  # noqa
        """Dispatch a request to the Razorpay HTTP API with retry mechanism."""
        options = self._update_user_agent_header(options)

        # Determine authentication type
        use_public_auth = options.pop("use_public_auth", False)
        auth_to_use = self.auth

        if use_public_auth:
            # For public auth, use key_id only
            if self.auth and isinstance(self.auth, tuple) and len(self.auth) >= 1:
                auth_to_use = (self.auth[0], "")  # Use key_id only, empty key_secret

        # Inject device mode header if provided
        device_mode = options.pop("device_mode", None)
        if device_mode:
            options.setdefault("headers", {})["X-Razorpay-Device-Mode"] = device_mode

        url = f"{self.base_url}{path}"

        delay_seconds = self.initial_delay

        # If retry is not enabled, set max attempts to 1
        max_attempts = self.max_retries if self.retry_enabled else 1

        for attempt in range(max_attempts):
            try:
                response = getattr(self.session, method)(
                    url, auth=auth_to_use, verify=self.cert_path, **options
                )

                if HttpStatusCode.OK <= response.status_code < HttpStatusCode.REDIRECT:
                    return (
                        json.dumps({})
                        if response.status_code == HttpStatusCode.NO_CONTENT
                        else response.json()
                    )

                try:
                    json_response = response.json()
                except ValueError as e:
                    msg = f"Non-JSON response: {response.text}"
                    raise ServerError(msg) from e

                error = json_response.get("error", {})
                msg = error.get("description", "")
                code = str(error.get("code", "")).upper()

                if code == ERROR_CODE.BAD_REQUEST_ERROR:
                    raise BadRequestError(msg)
                if code == ERROR_CODE.GATEWAY_ERROR:
                    raise GatewayError(msg)
                raise ServerError(msg)

            except (
                requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
            ) as e:
                if (
                    self.retry_enabled and attempt < max_attempts - 1
                ):  # Don't sleep on the last attempt
                    # Apply exponential backoff with jitter
                    jitter_value = random.uniform(  # noqa: S311
                        -self.jitter, self.jitter
                    )
                    actual_delay = min(delay_seconds * (1 + jitter_value), self.max_delay)

                    logger.warning(
                        f"{type(e).__name__}: {e}. Retrying in {actual_delay:.2f}s... "
                        f"(Attempt {attempt + 1}/{max_attempts})"
                    )
                    time.sleep(actual_delay)

                    delay_seconds = min(delay_seconds * 2, self.max_delay)
                    continue

                msg = f"{type(e).__name__} after {attempt + 1} attempts. " + (
                    "Retries disabled or exhausted." if not self.retry_enabled else ""
                )
                logger.error(msg)
                raise
            except requests.exceptions.RequestException as e:
                # For other request exceptions, don't retry
                logger.exception(f"Request error: {e}")
                raise
        return None

    def get(self, path, params, **options):
        """Parse GET request options and dispatch a request."""
        return self.request("get", path, params=params, **options)

    def post(self, path, data, **options):
        """Parse POST request options and dispatches a request."""
        data, options = self._update_request(data, options)
        return self.request("post", path, data=data, **options)

    def patch(self, path, data, **options):
        """Parse PATCH request options and dispatches a request."""
        data, options = self._update_request(data, options)
        return self.request("patch", path, data=data, **options)

    def delete(self, path, data, **options):
        """Parse DELETE request options and dispatches a request."""
        data, options = self._update_request(data, options)
        return self.request("delete", path, data=data, **options)

    def put(self, path, data, **options):
        """Parse PUT request options and dispatches a request."""
        data, options = self._update_request(data, options)
        return self.request("put", path, data=data, **options)

    def file(self, path, data, **options):
        """POST a file."""
        fileDict = {}
        fieldDict = {}

        if "file" not in data:
            # if file is not exists in the dictionary
            data["file"] = ""

        fileDict["file"] = data["file"]

        # Create a dict of form fields
        for fields in data:
            if fields != "file":
                fieldDict[str(fields)] = data[fields]

        return self.request("post", path, files=fileDict, data=fieldDict, **options)

    def _update_request(self, data, options):
        """Update The resource data and header options."""
        data = json.dumps(data)

        if "headers" not in options:
            options["headers"] = {}

        options["headers"].update({"Content-type": "application/json"})

        return data, options
