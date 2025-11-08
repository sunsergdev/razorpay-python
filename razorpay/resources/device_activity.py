"""Device activity resource."""

from __future__ import annotations

# Standard library imports
from typing import Any

# Razorpay SDK local imports
from ..constants.device import DeviceMode
from ..constants.url import URL
from ..errors import BadRequestError
from .base import Resource


class DeviceActivity(Resource):
    """Resource class for handling Razorpay DeviceActivity APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.DEVICE_ACTIVITY_URL

    def _validate_device_mode(self, device_mode: str | None) -> str | None:
        """
        Validate device communication mode.

        Args:
            device_mode: Device communication mode ("wired" or "wireless")

        Returns:
            Validated device_mode or None if device_mode is None

        Raises:
            BadRequestError: If device_mode is invalid
        """
        if device_mode is not None:
            if device_mode not in (DeviceMode.WIRED, DeviceMode.WIRELESS):
                msg = "Invalid device mode. Allowed values are 'wired' and 'wireless'."
                raise BadRequestError(msg)
            return device_mode
        return None

    def create(
        self, data: dict[str, Any], device_mode: str | None = None, **kwargs
    ) -> dict[str, Any]:
        """
        Create a new device activity for POS gateway.

        Args:
            data: Dictionary containing device activity data
                in the format expected by rzp-pos-gateway
            device_mode: Device communication mode ("wired" or "wireless")

        Returns:
            DeviceActivity object
        """
        validated_mode = self._validate_device_mode(device_mode)

        url = self.base_url
        return self.post(url, data, device_mode=validated_mode, use_public_auth=True, **kwargs)

    def get_status(
        self, activity_id: str, device_mode: str | None = None, **kwargs
    ) -> dict[str, Any]:
        """
        Get the status of a device activity.

        Args:
            activity_id: Activity ID to fetch status for
            device_mode: Device communication mode ("wired" or "wireless")

        Returns:
            DeviceActivity object with current status
        """
        if not activity_id:
            msg = "Activity ID must be provided"
            raise BadRequestError(msg)

        validated_mode = self._validate_device_mode(device_mode)

        url = f"{self.base_url}/{activity_id}"
        return self.get(url, {}, device_mode=validated_mode, use_public_auth=True, **kwargs)
