"""Plan resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Plan(Resource):
    """Resource class for handling Razorpay Plan APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.PLAN_URL

    def create(self, data=None, **kwargs):
        """Create Plan from given dict.

        Args:
            data : Dictionary having keys using which Plan has to be created

        Returns:
            Plan Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def fetch(self, plan_id, data=None, **kwargs):
        """Fetch Plan for given Id.

        Args:
            plan_id : Id for which Plan object has to be retrieved

        Returns:
            Plan dict for given subscription Id
        """
        if data is None:
            data = {}
        return super().fetch(plan_id, data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all plan entities.

        Returns:
            Dictionary of plan data
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)
