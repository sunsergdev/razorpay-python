"""PaymentLink resource."""

# Standard library imports
import warnings

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class PaymentLink(Resource):
    """Resource class for handling Razorpay PaymentLink APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.PAYMENT_LINK_URL

    def fetch_all(self, data=None, **kwargs):
        """Return all payment links."""
        if data is None:
            data = {}
        warnings.warn("Will be Deprecated in next release", DeprecationWarning, stacklevel=2)
        return self.all(data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all Payment link entities.

        Returns:
            Dictionary of Payment link data
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def fetch(self, payment_link_id, data=None, **kwargs):
        """Fetch Payment link for given Id.

        Args:
            payment_link_id : Id for which Payment link object has to be retrieved

        Returns:
            Payment link dict for given payment_link_id Id
        """
        if data is None:
            data = {}
        return super().fetch(payment_link_id, data, **kwargs)

    def create(self, data=None, **kwargs):
        """Create Payment link from given dict.

        Args:
            data : Dictionary having keys using which Payment link have to be created

        Returns:
            Payment link Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def cancel(self, payment_link_id, **kwargs):
        """Cancel an unpaid Payment link with given ID via API.

        It can only be called on a Payment link that is not in the paid state.

        Args:
            payment_link_id : Id for cancel the Payment link

        Returns:
            The response for the API will be the Payment link entity, similar to create/update API
            response, with status attribute's value as cancelled
        """
        url = f"{self.base_url}/{payment_link_id}/cancel"
        return self.post(url, {}, **kwargs)

    def edit(self, payment_link_id, data=None, **kwargs):
        """Edit the Payment link.

        Args:
            data : Dictionary having keys using which order have to be edited
                reference_id : Adds a unique reference number to an existing link.
                expire_by : Timestamp, in Unix format, when the payment links should expire.
                notes : key value pair as notes

        Returns:
            Payment Link Dict which was edited
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_link_id}"
        return self.patch(url, data, **kwargs)

    def notifyBy(self, payment_link_id, medium, **kwargs):
        """Send notification.

        Args:
            payment_link_id : Unique identifier of the Payment Link that should be resent.
            medium : sms/email
        """
        url = f"{self.base_url}/{payment_link_id}/notify_by/{medium}"
        return self.post(url, {}, **kwargs)
