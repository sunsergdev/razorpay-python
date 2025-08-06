"""Stakeholder resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Stakeholder(Resource):
    """Resource class for handling Razorpay Stakeholder APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V2 + URL.ACCOUNT

    def create(self, account_id, data=None, **kwargs):
        """Create stakeholder from given dict and account id.

        Args:
            account_id : Id for which account object has to be retrieved

        Returns:
            Stakeholder Dict which was created
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{account_id}{URL.STAKEHOLDER}"
        return self.post(url, data, **kwargs)

    def fetch(self, account_id, stakeholder_id, data=None, **kwargs):
        """Fetch stakeholder for given account & stakeholder id.

        Args:
            account_id : Id for which account object has to be retrieved
            stakeholder_id : Id for which stakeholder object has to be retrieved

        Returns:
            stakeholder dict for given account_id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{account_id}{URL.STAKEHOLDER}/{stakeholder_id}"
        return self.get(url, data, **kwargs)

    def all(self, account_id, data=None, **kwargs):
        """Fetch all stakeholders for an account.

        Args:
            account_id : Id for which account object has to be retrieved

        Returns:
            stakeholder dict for given account_id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{account_id}{URL.STAKEHOLDER}"
        return self.get(url, data, **kwargs)

    def edit(self, account_id, stakeholder_id, data=None, **kwargs):
        """Edit stakeholder information from given dict.

        Args:
            account_id : Id for which account object has to be retrieved
            stakeholder_id : Id for which stakeholder object has to be edited

        Returns:
            Stakeholder Dict which was edited
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{account_id}{URL.STAKEHOLDER}/{stakeholder_id}"
        return self.patch(url, data, **kwargs)

    def uploadStakeholderDoc(self, account_id, stakeholder_id, data=None, **kwargs):
        """Upload Stakeholder Documents.

        Args:
            account_id : Id for which account object has to be retrieved
            stakeholder_id : Id for which stakeholder object has to be edited

        Returns:
           Stakeholder Document dict which was created
        """
        if data is None:
            data = {}
        url = "{}/{}{}/{}/{}".format(
            self.base_url, account_id, URL.STAKEHOLDER, stakeholder_id, "documents"
        )
        return self.file(url, data, **kwargs)

    def fetchStakeholderDoc(self, account_id, stakeholder_id, data=None, **kwargs):
        """Fetch Stakeholder Documents.

        Args:
            account_id : Id for which account object has to be retrieved
            stakeholder_id : Id for which stakeholder object has to be retrieved

        Returns:
            Stakeholder Document dict for given account & stakeholder Id
        """
        if data is None:
            data = {}
        url = "{}/{}{}/{}/{}".format(
            self.base_url, account_id, URL.STAKEHOLDER, stakeholder_id, "documents"
        )
        return self.get(url, data, **kwargs)
