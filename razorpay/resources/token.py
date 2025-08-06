"""Token resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Token(Resource):
    """Resource class for handling Razorpay Token APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.CUSTOMER_URL

    def create(self, data=None, **kwargs):
        """Create token from given dict.

        Returns:
            token Dict which was created
        """
        if data is None:
            data = {}
        url = f"{URL.V1}{URL.TOKEN}"
        return self.post(url, data, **kwargs)

    def fetch(self, customer_id, token_id, data=None, **kwargs):
        """Fetch Token for given Id and given customer Id.

        Args:
            customer_id : Customer Id for which tokens have to be fetched
            token_id    : Id for which Token object has to be fetched

        Returns:
            Token dict for given token Id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{customer_id}/tokens/{token_id}"
        return self.get(url, data, **kwargs)

    def all(self, customer_id, data=None, **kwargs):
        """Get all tokens for given customer Id.

        Args:
            customer_id : Customer Id for which tokens have to be fetched

        Returns:
            Token dicts for given customer Id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{customer_id}/tokens"
        return self.get(url, data, **kwargs)

    def delete(self, customer_id, token_id, data=None, **kwargs):
        """Delete Given Token For a Customer.

        Args:
            customer_id : Customer Id for which tokens have to be deleted
            token_id    : Id for which Token object has to be deleted

        Returns:
            Dict for deleted token
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{customer_id}/tokens/{token_id}"
        return self.delete_url(url, data, **kwargs)

    def fetchToken(self, data=None, **kwargs):
        """Fetch Given Token For a Customer.

        Returns:
            Dict for fetch token
        """
        if data is None:
            data = {}
        url = "{}{}/{}".format(URL.V1, URL.TOKEN, "fetch")
        return self.post(url, data, **kwargs)

    def deleteToken(self, data=None, **kwargs):
        """Delete Given Token.

        Returns:
            Dict for deleted token
        """
        if data is None:
            data = {}
        url = "{}{}/{}".format(URL.V1, URL.TOKEN, "delete")
        return self.post(url, data, **kwargs)

    def processPaymentOnAlternatePAorPG(self, data=None, **kwargs):
        """Process a Payment on another PA/PG with Token Created on Razorpay."""
        if data is None:
            data = {}
        url = "{}{}/{}".format(
            URL.V1, URL.TOKEN, "service_provider_tokens/token_transactional_data"
        )
        return self.post(url, data, **kwargs)
