"""FundAccount resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class FundAccount(Resource):
    """Resource class for handling Razorpay FundAccount APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.FUND_ACCOUNT_URL

    def all(self, data=None, **kwargs):
        """Fetch all Fund Account entities.

        Returns:
            Dictionary of Fund Account
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def create(self, data=None, **kwargs):
        """Create a fund account.

        Args:
            data : Dictionary having keys using which order have to be created
                'customerId' :  Customer Id for the customer
                'account_type' : The bank_account to be linked to the customer ID
                'bank_account' : key value pair

        Returns:
            fund account Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)
