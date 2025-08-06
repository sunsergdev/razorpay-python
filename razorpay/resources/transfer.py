"""Transfer resource."""

# Standard library imports
import warnings

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Transfer(Resource):
    """Resource class for handling Razorpay Transfer APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.TRANSFER_URL

    def fetch_all(self, data=None, **kwargs):
        """Return all transfers."""
        if data is None:
            data = {}
        warnings.warn(
            "Will be Deprecated in next release, use all",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.all(data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all Transfer entities.

        Returns:
            Dictionary of Transfer data
        """
        if data is None:
            data = {}
        if "payment_id" in data:
            url = URL.V1 + "/payments/{}/transfers".format(data["payment_id"])

            del data["payment_id"]
            return self.get(url, data, **kwargs)

        return super().all(data, **kwargs)

    def fetch(self, transfer_id, data=None, **kwargs):
        """Fetch Transfer for given Id.

        Args:
            transfer_id : Id for which transfer object has to be retrieved

        Returns:
            Transfer dict for given transfer Id
        """
        if data is None:
            data = {}
        return super().fetch(transfer_id, data, **kwargs)

    def create(self, data=None, **kwargs):
        """Create Transfer from given dict.

        Returns:
            Transfer Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def edit(self, transfer_id, data=None, **kwargs):
        """Edit Transfer from given id.

        Args:
            transfer_id : Id for which transfer object has to be edited

        Returns:
            Transfer Dict which was edited
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{transfer_id}"
        return self.patch(url, data, **kwargs)

    def reverse(self, transfer_id, data=None, **kwargs):
        """Reverse Transfer from given id.

        Args:
            transfer_id : Id for which transfer object has to be reversed

        Returns:
            Transfer Dict which was reversed
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{transfer_id}/reversals"
        return self.post(url, data, **kwargs)

    def reversals(self, transfer_id, data=None, **kwargs):
        """Get all Reversal Transfer from given id.

        Args:
            transfer_id :
                Id for which reversal transfer object has to be fetched

        Returns:
            Transfer Dict
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{transfer_id}/reversals"
        return self.get(url, data, **kwargs)
