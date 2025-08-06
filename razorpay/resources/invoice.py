"""Invoice resource."""

# Standard library imports
import warnings

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Invoice(Resource):
    """Resource class for handling Razorpay Invoice APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.INVOICE_URL

    def fetch_all(self, data=None, **kwargs):
        """Fetch all invoices.

        Returns:
            List of all invoices
        """
        if data is None:
            data = {}
        warnings.warn("Will be Deprecated in next release", DeprecationWarning, stacklevel=2)
        return self.all(data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all Invoice entities.

        Returns:
            Dictionary of Invoice data
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def fetch(self, invoice_id, data=None, **kwargs):
        """Fetch Invoice for given Id.

        Args:
            invoice_id : Id for which invoice object has to be retrieved

        Returns:
            Invoice dict for given invoice Id
        """
        if data is None:
            data = {}
        return super().fetch(invoice_id, data, **kwargs)

    def create(self, data=None, **kwargs):
        """Create Invoice from given dict.

        Args:
            data : Dictionary having keys using which invoice have to be created

        Returns:
            Invoice Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def notify_by(self, invoice_id, medium, **kwargs):
        """Send/Resend notifications to customer via email/sms.

        Args:
            invoice_id : Id for trigger notify
            medium : Medium for triggering notification via email or sms

        Returns:
            {"success": true}
        """
        url = f"{self.base_url}/{invoice_id}/notify_by/{medium}"
        return self.post(url, {}, **kwargs)

    def cancel(self, invoice_id, **kwargs):
        """Cancel an unpaid Invoice with given ID via API.

        It can only be called on an invoice that is not in the paid state.

        Args:
            invoice_id : Id for cancel the invoice

        Returns:
            The response for the API will be the invoice entity,
            similar to create/update API response, with status attribute's value as cancelled
        """
        url = f"{self.base_url}/{invoice_id}/cancel"
        return self.post(url, {}, **kwargs)

    def delete(self, invoice_id, **kwargs):
        """Delete an invoice.

        You can delete an invoice which is in the draft state.

        Args:
            invoice_id : Id for delete the invoice

        Returns:
            The response is always be an empty array like this - []
        """
        url = f"{self.base_url}/{invoice_id}"
        return self.delete_url(url, {}, **kwargs)

    def issue(self, invoice_id, **kwargs):
        """Issues an invoice in draft state.

        Args:
            invoice_id : Id for the invoice to issue

        Returns:
            Its response is the invoice entity, similar to create/update API response.
            Its status now would be issued.
        """
        url = f"{self.base_url}/{invoice_id}/issue"
        return self.post(url, {}, **kwargs)

    def edit(self, invoice_id, data=None, **kwargs):
        """Update an invoice.

        In draft state all the attributes are allowed.

        Args:
            invoice_id : Id for the invoice to update
            data : Dictionary having keys using which invoice have to be updated

        Returns:
            Its response is the invoice entity, similar to create/update API response.
            Its status now would be issued. Refer https://razorpay.com/docs/invoices/api/#entity-structure
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{invoice_id}"
        return self.patch(url, data, **kwargs)
