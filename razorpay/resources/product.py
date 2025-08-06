"""Product resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Product(Resource):
    """Resource class for handling Razorpay Product APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V2 + URL.ACCOUNT

    def requestProductConfiguration(self, account_id, data=None, **kwargs):
        """Request a Product Configuration from given dict.

        Args:
            account_id : Id for which account object has to be retrieved

        Returns:
            Product Configuration Dict which was created
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{account_id}{URL.PRODUCT}"
        return self.post(url, data, **kwargs)

    def fetch(self, account_id, product_id, data=None, **kwargs):
        """Fetch product for given account and product id.

        Args:
            account_id : Id for which account object has to be retrieved
            product_id : Id for which product object has to be retrieved

        Returns:
            account dict for given account_id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{account_id}{URL.PRODUCT}/{product_id}"
        return self.get(url, data, **kwargs)

    def edit(self, account_id, product_id, data=None, **kwargs):
        """Edit account information from given dict.

        Args:
            account_id : Id for which account object has to be retrieved
            product_id : Id for which product object has to be edited

        Returns:
            Account Dict which was edited
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{account_id}{URL.PRODUCT}/{product_id}"
        return self.patch(url, data, **kwargs)

    def fetchTnc(self, product_name, data=None, **kwargs):
        """Fetch Terms and Conditions for a Sub-Merchant.

        Args:
            product_name : Name of the product for which TnC is fetched

        Returns:
            Tnc dict for given account_id
        """
        if data is None:
            data = {}
        url = f"{URL.V2}{URL.PRODUCT}/{product_name}{URL.TNC}"
        return self.get(url, data, **kwargs)
