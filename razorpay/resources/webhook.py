"""Webhook resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Webhook(Resource):
    """Resource class for handling Razorpay Webhook APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V2 + URL.ACCOUNT

    def create(self, data=None, account_id=None, **kwargs):
        """Create webhook from given dict.

        Returns:
            Webhook Dict which was created
        """
        data = data or {}

        if account_id is None:
            url = f"{URL.V1}{URL.WEBHOOK}"
        else:
            url = f"{self.base_url}/{account_id}{URL.WEBHOOK}"

        return self.post(url, data, **kwargs)

    def fetch(self, webhook_id, account_id, data=None, **kwargs):
        """Fetch webhook for given webhook id.

        Args:
            account_id : Id for which webhook object has to be retrieved
            webhook_id : Id for which account object has to be retrieved

        Returns:
            webhook dict for given webhook_id
        """
        data = data or {}

        if account_id:
            url = f"{self.base_url}/{account_id}{URL.WEBHOOK}/{webhook_id}"
        else:
            url = f"{URL.V1}{URL.WEBHOOK}/{webhook_id}"

        return self.get(url, data, **kwargs)

    def all(self, data=None, account_id=None, **kwargs):
        """Fetch all webhooks.

        Args:
            account_id : Id for which webhook object has to be retrieved

        Returns:
            webhook dict for given account_id
        """
        data = data or {}

        if account_id is None:
            url = f"{URL.V1}{URL.WEBHOOK}"
        else:
            url = f"{self.base_url}/{account_id}{URL.WEBHOOK}"

        return self.get(url, data, **kwargs)

    def edit(self, webhook_id, account_id, data=None, **kwargs):
        """Edit webhook from given dict.

        Returns:
            Webhook Dict which was edited
        """
        data = data or {}

        if account_id:
            url = f"{self.base_url}/{account_id}{URL.WEBHOOK}/{webhook_id}"
            return self.patch(url, data, **kwargs)

        url = f"{URL.V1}{URL.WEBHOOK}/{webhook_id}"
        return self.put(url, data, **kwargs)

    def delete(self, webhook_id, account_id, data=None, **kwargs):
        """Delete webhook for given webhook id.

        Args:
            account_id : Id for which webhook object has to be retrieved
            webhook_id : Id for which account object has to be retrieved

        Returns:
            The response is always be an empty array like this - []
        """
        data = data or {}
        url = f"{self.base_url}/{account_id}{URL.WEBHOOK}/{webhook_id}"
        return self.delete_url(url, data, **kwargs)
