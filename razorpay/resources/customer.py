"""Customer resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Customer(Resource):
    """Resource class for handling Razorpay Customer APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.CUSTOMER_URL

    def fetch(self, customer_id, data=None, **kwargs):
        """Fetch Customer for given Id.

        Args:
            customer_id : Id for which customer object has to be retrieved

        Returns:
            Customer dict for given customer Id
        """
        if data is None:
            data = {}
        return super().fetch(customer_id, data, **kwargs)

    def create(self, data=None, **kwargs):
        """Create Customer from given dict.

        Returns:
            Customer Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def edit(self, customer_id, data=None, **kwargs):
        """Edit Customer information from given dict.

        Returns:
            Customer Dict which was edited
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{customer_id}"
        return self.put(url, data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all customers.

        Returns:
            Dictionary of Customers data
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def addBankAccount(self, customer_id, data=None, **kwargs):
        """Add Bank Account of Customer.

        Returns:
            Dictionary of Customers data
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{customer_id}/bank_account"
        return self.post(url, data, **kwargs)

    def deleteBankAccount(self, customer_id, bank_id, data=None, **kwargs):
        """Delete Bank Account of Customer.

        Returns:
            Dictionary of Customers data
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{customer_id}/bank_account/{bank_id}"
        return self.delete_url(url, data, **kwargs)

    def requestEligibilityCheck(self, data=None, **kwargs):
        """Eligibility Check.

        Returns:
            Dictionary of eligibility data
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/eligibility"
        return self.post(url, data, **kwargs)

    def fetchEligibility(self, eligibility_id, data=None, **kwargs):
        """Fetch Eligibility by id.

        Returns:
            Eligibility dict for given eligibility Id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/eligibility/{eligibility_id}"
        return self.get(url, data, **kwargs)
