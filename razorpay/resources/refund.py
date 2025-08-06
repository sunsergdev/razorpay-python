"""Refund resource."""

# Standard library imports
import warnings

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Refund(Resource):
    """Resource class for handling Razorpay Refund APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.REFUNDS_URL

    def fetch_all(self, data=None, **kwargs):
        """Return all refunds.

        Returns:
            List of all refunds
        """
        if data is None:
            data = {}
        warnings.warn(
            "Will be Deprecated in next release, use all",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.all(data, **kwargs)

    def create(self, data=None, **kwargs):
        """Create refund for given payment id.

        Returns:
            Refund dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all refunds.

        Returns:
            Refund dict
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def fetch(self, refund_id, data=None, **kwargs):
        """Fetch refund object for given refund Id.

        Args:
            refund_id : Refund Id for which refund has to be retrieved

        Returns:
            Refund dict for given refund Id
        """
        if data is None:
            data = {}
        return super().fetch(refund_id, data, **kwargs)

    def edit(self, refund_id, data=None, **kwargs):
        """Update refund.

        Returns:
            Refund Dict which was edited
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{refund_id}"
        return self.patch(url, data, **kwargs)
