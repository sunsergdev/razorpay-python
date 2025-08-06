"""Razorpay client."""

# Standard library imports
import json
import os
from importlib.metadata import PackageNotFoundError, version
from types import ModuleType

# Other third-party library imports
import requests

# Razorpay SDK local imports
from . import resources, utility
from .constants import ERROR_CODE, URL
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


class Client:
    """Razorpay client class."""

    DEFAULTS = {"base_url": URL.BASE_URL}  # noqa: RUF012

    def __init__(self, session=None, auth=None, **options):
        self.session = session or requests.Session()
        self.auth = auth
        file_dir = os.path.dirname(__file__)
        self.cert_path = file_dir + "/ca-bundle.crt"

        self.base_url = self._set_base_url(**options)

        self.app_details = []

        # intializes each resource
        # injecting this client object into the constructor
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

        for name, Klass in UTILITY_CLASSES.items():
            setattr(self, name, Klass(self))

    def _set_base_url(self, **options):
        base_url = self.DEFAULTS["base_url"]

        if "base_url" in options:
            base_url = options["base_url"]
            del options["base_url"]

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
        except PackageNotFoundError:
            return ""

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

    def request(self, method, path, **options):
        """Invoke a request to the Razorpay HTTP API."""
        options = self._update_user_agent_header(options)

        url = f"{self.base_url}{path}"

        response = getattr(self.session, method)(
            url, auth=self.auth, verify=self.cert_path, **options
        )
        if (response.status_code >= requests.codes.ok) and (
            response.status_code < requests.codes.multiple_choices
        ):
            return (
                json.dumps({})
                if (response.status_code == requests.codes.no_content)
                else response.json()
            )
        msg = ""
        code = ""
        json_response = response.json()
        if "error" in json_response:
            if "description" in json_response["error"]:
                msg = json_response["error"]["description"]
            if "code" in json_response["error"]:
                code = str(json_response["error"]["code"])

        if str.upper(code) == ERROR_CODE.BAD_REQUEST_ERROR:
            raise BadRequestError(msg)
        if str.upper(code) == ERROR_CODE.GATEWAY_ERROR:
            raise GatewayError(msg)
        raise ServerError(msg)

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
