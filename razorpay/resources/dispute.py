"""Dispute resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Dispute(Resource):
    """Resource class for handling Razorpay Dispute APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.DISPUTE

    def fetch(self, dispute_id, data=None, **kwargs):
        """Fetch dispute for given Id.

        Args:
            dispute_id : Id for which dispute object has to be retrieved

        Returns:
            dispute dict for given dispute Id
        """
        if data is None:
            data = {}
        return super().fetch(dispute_id, data, **kwargs)

    def accept(self, dispute_id, data=None, **kwargs):
        """Accept a dispute.

        Args:
            dispute_id : Id for which dispute object has to be accepted

        Returns:
             Dictionary of disputes
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{dispute_id}/accept"
        return self.post(url, data, **kwargs)

    def contest(self, dispute_id, data=None, **kwargs):
        """Contest a Dispute.

        Args:
            dispute_id : Id for which dispute object has to be contested

        Returns:
             Dictionary of disputes
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{dispute_id}/contest"
        return self.patch(url, data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all disputes.

        Returns:
            Dictionary of disputes
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)
