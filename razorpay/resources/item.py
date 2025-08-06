"""Item resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Item(Resource):
    """Resource class for handling Razorpay Item APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.ITEM_URL

    def create(self, data=None, **kwargs):
        """Create item.

        Returns:
            Item Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def fetch(self, item_id, data=None, **kwargs):
        """Fetch an Item.

        Args:
            item_id : The id of the item to be fetched

        Returns:
            Item dict for given item Id
        """
        if data is None:
            data = {}
        return super().fetch(item_id, data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all items.

        Returns:
            Dictionary of Items data
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def edit(self, item_id, data=None, **kwargs):
        """Update an Item.

        Returns:
            Item Dict which was edited
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{item_id}"
        return self.patch(url, data, **kwargs)

    def delete(self, item_id, **kwargs):
        """Delete an Item.

        Args:
            item_id : The id of the item to be deleted

        Returns:
            The response is always an empty array like this - []
        """
        url = f"{self.base_url}/{item_id}"
        return self.delete_url(url, {}, **kwargs)
