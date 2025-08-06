"""Addon resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Addon(Resource):
    """Resource class for handling Razorpay Addon APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.ADDON_URL

    def fetch(self, addon_id, data=None, **kwargs):
        """Fetch addon for given Id.

        Args:
            addon_id : Id for which addon object has to be retrieved

        Returns:
            addon dict for given subscription Id
        """
        if data is None:
            data = {}
        return super().fetch(addon_id, data, **kwargs)

    def delete(self, addon_id, data=None, **kwargs):
        """Delete addon for given id.

        Args:
            addon_id : Id for which addon object has to be deleted
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{addon_id}"

        return self.delete_url(url, data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all Add-ons.

        Returns:
            Dictionary of Add-ons
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)
