"""Subscription resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Subscription(Resource):
    """Resource class for handling Razorpay Subscription APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.SUBSCRIPTION_URL

    def all(self, data=None, **kwargs):
        """Fetch all Subscription entities.

        Returns:
            Dictionary of Subscription data
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def fetch(self, subscription_id, data=None, **kwargs):
        """Fetch Subscription for given Id.

        Args:
            subscription_id : Id for which subscription object is retrieved

        Returns:
            Subscription dict for given subscription Id
        """
        if data is None:
            data = {}
        return super().fetch(subscription_id, data, **kwargs)

    def create(self, data=None, **kwargs):
        """Create Subscription from given dict.

        Args:
            data : Dictionary using which Subscription has to be created

        Returns:
            Subscription Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def cancel(self, subscription_id, data=None, **kwargs):
        """Cancel subscription given by subscription_id.

        Args:
            subscription_id : Id for which subscription has to be cancelled

        Returns:
            Subscription Dict for given subscription id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{subscription_id}/cancel"
        return self.post(url, data, **kwargs)

    def cancel_scheduled_changes(self, subscription_id, data=None, **kwargs):
        """Cancel a scheduled update.

        Args:
            subscription_id : Id for which subscription has to be cancelled

        Returns:
            Subscription Dict for given subscription id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{subscription_id}/cancel_scheduled_changes"
        return self.post(url, data, **kwargs)

    def createAddon(self, subscription_id, data=None, **kwargs):
        """Create addon for given subscription.

        Args:
            subscription_id : Id for which addon has to be created

        Returns:
            Subscription dict for given subscription id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{subscription_id}/addons"
        return self.post(url, data, **kwargs)

    def edit(self, subscription_id, data=None, **kwargs):
        """Update particular subscription.

        Args:
            subscription_id : Id for which subscription has to be edited

        Returns:
            Subscription dict for given subscription id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{subscription_id}"
        return self.patch(url, data, **kwargs)

    def pending_update(self, subscription_id, **kwargs):
        """Fetch pending update for given subscription Id.

        Args:
            subscription_id : Id for which subscription object is retrieved

        Returns:
            Subscription dict for given subscription Id
        """
        url = f"{self.base_url}/{subscription_id}/retrieve_scheduled_changes"
        return self.get(url, {}, **kwargs)

    def pause(self, subscription_id, data=None, **kwargs):
        """Pause subscription given by subscription_id.

        Args:
            subscription_id : Id for which subscription has to be paused

        Returns:
            Subscription Dict for given subscription id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{subscription_id}/pause"
        return self.post(url, data, **kwargs)

    def resume(self, subscription_id, data=None, **kwargs):
        """Resume subscription given by subscription_id.

        Args:
            subscription_id : Id for which subscription has to be resumed

        Returns:
            Subscription Dict for given subscription id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{subscription_id}/resume"
        return self.post(url, data, **kwargs)

    def delete_offer(self, subscription_id, offer_id, data=None, **kwargs):
        """Delete offer linked to a subscription.

        Args:
            subscription_id : The id of the subscription to offer need to be deleted
            offer_id : The id of the offer linked to subscription

        Returns:
            Subscription Dict for given subscription id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{subscription_id}/{offer_id}"
        return self.delete_url(url, data, **kwargs)
