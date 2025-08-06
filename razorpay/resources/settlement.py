"""Settlement resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Settlement(Resource):
    """Resource class for handling Razorpay Settlement APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.SETTLEMENT_URL

    def all(self, data=None, **kwargs):
        """Fetch all Settlement entities.

        Returns:
            Dictionary of Settlement data
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def fetch(self, settlement_id, data=None, **kwargs):
        """Fetch Settlement data for given Id.

        Args:
            settlement_id : Id for which settlement object has to be retrieved

        Returns:
            settlement dict for given settlement id
        """
        if data is None:
            data = {}
        return super().fetch(settlement_id, data, **kwargs)

    def report(self, data=None, **kwargs):
        """Settlement report for a month.

        Returns:
            settlement dict
        """
        if data is None:
            data = {}
        url = "{}/recon/{}".format(self.base_url, "combined")
        return self.get(url, data, **kwargs)

    def create_ondemand_settlement(self, data=None, **kwargs):
        """Create Ondemand Settlement entity.

        Returns:
            settlement dict which was created
        """
        if data is None:
            data = {}
        url = "{}/{}".format(self.base_url, "ondemand")
        return self.post(url, data, **kwargs)

    def fetch_all_ondemand_settlement(self, data=None, **kwargs):
        """Fetch all Ondemand Settlement entities.

        Returns:
            settlement dict which was created
        """
        if data is None:
            data = {}
        url = "{}/{}".format(self.base_url, "ondemand")
        return self.get(url, data, **kwargs)

    def fetch_ondemand_settlement_id(self, settlement_id, data=None, **kwargs):
        """Fetch Ondemand Settlement by Id.

        Returns:
            settlement dict for given settlement id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/ondemand/{settlement_id}"
        return self.get(url, data, **kwargs)
