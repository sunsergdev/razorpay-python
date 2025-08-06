"""Iin resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Iin(Resource):
    """Resource class for handling Razorpay IIN APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.IIN

    def fetch(self, token_iin, data=None, **kwargs):
        """Fetch card properties using token iin.

        Args:
            token_iin : The IIN (Issuer Identification Number) to fetch properties for

        Returns:
            Iin dict for given token iin
        """
        if data is None:
            data = {}
        return super().fetch(token_iin, data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all iins supporting native otp with business sub-type.

        Returns:
            Dictionary of Iin data
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/list"
        return self.get(url, data, **kwargs)
