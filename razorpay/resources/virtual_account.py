"""Virtual account resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class VirtualAccount(Resource):
    """Resource class for handling Razorpay VirtualAccount APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.VIRTUAL_ACCOUNT_URL

    def all(self, data=None, **kwargs):
        """Fetch all Virtual Account entities.

        Returns:
            Dictionary of Virtual Account data
        """
        data = data or {}
        return super().all(data, **kwargs)

    def fetch(self, virtual_account_id, data=None, **kwargs):
        """Fetch Virtual Account for given Id.

        Args:
            virtual_account_id :
                Id for which Virtual Account object has to be retrieved

        Returns:
            Virtual Account dict for given Virtual Account Id
        """
        data = data or {}
        return super().fetch(virtual_account_id, data, **kwargs)

    def create(self, data=None, **kwargs):
        """Create Virtual Account from given dict.

        Args:
            Param for Creating Virtual Account

        Returns:
            Virtual Account dict
        """
        data = data or {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def close(self, virtual_account_id, data=None, **kwargs):
        """Close Virtual Account from given Id.

        Args:
            virtual_account_id :
                Id for which Virtual Account objects has to be Closed
        """
        data = data or {}
        url = f"{self.base_url}/{virtual_account_id}/close"
        return self.post(url, data, **kwargs)

    def payments(self, virtual_account_id, data=None, **kwargs):
        """Fetch Payment for Virtual Account Id.

        Args:
            virtual_account_id :
                Id for which Virtual Account objects has to be retrieved

        Returns:
            Payment dict for given Virtual Account Id
        """
        data = data or {}
        url = f"{self.base_url}/{virtual_account_id}/payments"
        return self.get(url, data, **kwargs)

    def add_receiver(self, virtual_account_id, data=None, **kwargs):
        """Add receiver to an existing virtual account.

        Args:
            virtual_account_id :
                Id for which Virtual Account objects has to be Closed
        """
        data = data or {}
        url = f"{self.base_url}/{virtual_account_id}/receivers"
        return self.post(url, data, **kwargs)

    def add_allowed_player(self, virtual_account_id, data=None, **kwargs):
        """Add an Allowed Payer Account.

        Args:
            virtual_account_id :
                Id for which Virtual Account objects has to be Closed
        """
        data = data or {}
        url = f"{self.base_url}/{virtual_account_id}/allowed_payers"
        return self.post(url, data, **kwargs)

    def delete_allowed_player(self, virtual_account_id, allowed_player_id, data=None, **kwargs):
        """Delete an Allowed Payer Account.

        Args:
            virtual_account_id :
                Id for which Virtual Account objects has to be Closed

        Returns:
            204
        """
        data = data or {}
        url = f"{self.base_url}/{virtual_account_id}/allowed_payers/{allowed_player_id}"
        return self.delete_url(url, data, **kwargs)
