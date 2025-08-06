"""Account resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Account(Resource):
    """Resource class for handling Razorpay Account APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V2 + URL.ACCOUNT

    def create(self, data=None, **kwargs):
        """Create account from given dict.

        Returns:
            Account Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def fetch(self, account_id, data=None, **kwargs):
        """Fetch account for given Id.

        Args:
            account_id : Id for which addon object has to be retrieved

        Returns:
            account dict for given account_id
        """
        if data is None:
            data = {}
        return super().fetch(account_id, data, **kwargs)

    def edit(self, account_id, data=None, **kwargs):
        """Edit account information from given dict.

        Returns:
            Account Dict which was edited
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{account_id}"
        return self.patch(url, data, **kwargs)

    def delete(self, account_id, data=None, **kwargs):
        """Delete account for given id.

        Args:
            account_id : Id for which account object has to be deleted
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{account_id}"
        return self.delete_url(url, data, **kwargs)

    def uploadAccountDoc(self, account_id, data=None, **kwargs):
        """Upload Account Documents.

        Returns:
           Account Document dict which was created
        """
        if data is None:
            data = {}
        url = "{}/{}/{}".format(self.base_url, account_id, "documents")
        return self.file(url, data, **kwargs)

    def fetchAccountDoc(self, account_id, data=None, **kwargs):
        """Fetch Account Documents.

        Returns:
            Account Document dict for given account_id
        """
        if data is None:
            data = {}
        url = "{}/{}/{}".format(self.base_url, account_id, "documents")

        return self.get(url, data, **kwargs)
