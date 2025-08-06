"""Card resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Card(Resource):
    """Resource class for handling Razorpay Card APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.CARD_URL

    def fetch(self, card_id, data=None, **kwargs):
        """Fetch Card for given Id.

        Args:
            card_id : Id for which card object has to be retrieved

        Returns:
            Card dict for given card Id
        """
        if data is None:
            data = {}
        return super().fetch(card_id, data, **kwargs)

    def requestCardReference(self, data=None, **kwargs):
        """Fetch card reference number for a specific card.

        Args:
            number : The card number whose PAR or network reference id should be retrieved.

        Returns:
            Card dict for given card Id
        """
        if data is None:
            data = {}
        url = "{}/{}".format(self.base_url, "fingerprints")
        return self.post(url, data, **kwargs)
