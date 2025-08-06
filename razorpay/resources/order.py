"""Order resource."""

# Standard library imports
import warnings

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Order(Resource):
    """Resource class for handling Razorpay Order APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.ORDER_URL

    def fetch_all(self, data=None, **kwargs):
        """Fetch all orders.

        Returns:
            List of all orders
        """
        if data is None:
            data = {}
        warnings.warn(
            "Will be Deprecated in next release, use all",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.all(data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all Order entities.

        Returns:
            Dictionary of Order data
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def fetch(self, order_id, data=None, **kwargs):
        """Fetch Order for given Id.

        Args:
            order_id : Id for which order object has to be retrieved

        Returns:
            Order dict for given order Id
        """
        if data is None:
            data = {}
        return super().fetch(order_id, data, **kwargs)

    def fetch_all_payments(self, order_id, data=None, **kwargs):
        """Fetch all payments for an order.

        Returns:
            List of all payments for the order
        """
        if data is None:
            data = {}
        warnings.warn(
            "Will be Deprecated in next release, use payments",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.payments(order_id, data, **kwargs)

    def payments(self, order_id, data=None, **kwargs):
        """Fetch Payment for Order Id.

        Args:
            order_id : Id for which payment objects has to be retrieved

        Returns:
            Payment dict for given Order Id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{order_id}/payments"
        return self.get(url, data, **kwargs)

    def create(self, data=None, **kwargs):
        """Create Order from given dict.

        Args:
            data : Dictionary having keys using which order have to be created
                'amount' :  Amount of Order
                'currency' : Currency used in Order
                'receipt' : Receipt Id for the order
                'notes' : key value pair as notes
                'payment_capture': 0/1 if payment should be auto captured or not

        Returns:
            Order Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def edit(self, order_id, data=None, **kwargs):
        """Update order.

        Args:
            data : Dictionary having keys using which order have to be edited
                'notes' : key value pair as notes

        Returns:
            Order Dict which was edited
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{order_id}"
        return self.patch(url, data, **kwargs)

    def viewRtoReview(self, order_id, data=None, **kwargs):
        """View rto risk reasons.

        Returns:
            Dict for given Order Id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{order_id}/rto_review"
        return self.post(url, data, **kwargs)

    def editFulfillment(self, order_id, data=None, **kwargs):
        """Update the Fulfillment Details.

        Returns:
            Dict for given Order Id
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{order_id}/fulfillment"
        return self.post(url, data, **kwargs)
