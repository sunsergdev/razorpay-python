"""Payment resource."""

# Standard library imports
import warnings

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Payment(Resource):
    """Resource class for handling Razorpay Payment APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.PAYMENTS_URL

    def fetch_all(self, data=None, **kwargs):
        """Fetch all payments."""
        if data is None:
            data = {}
        warnings.warn(
            "Will be Deprecated in next release, use all",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.all(data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all Payment entities.

        Returns:
            Dictionary of Payment data
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def fetch(self, payment_id, data=None, **kwargs):
        """Fetch Payment for given Id.

        Args:
            payment_id : Id for which payment object has to be retrieved

        Returns:
            Payment dict for given payment Id
        """
        if data is None:
            data = {}
        return super().fetch(payment_id, data, **kwargs)

    def capture(self, payment_id, amount, data=None, **kwargs):
        """Capture Payment for given Id.

        Args:
            payment_id : Id for which payment object has to be retrieved
            amount : Amount for which the payment has to be retrieved

        Returns:
            Payment dict after getting captured
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_id}/capture"
        data["amount"] = amount
        return self.post(url, data, **kwargs)

    def transfer(self, payment_id, data=None, **kwargs):
        """Create Transfer for given Payment Id.

        Args:
            payment_id : Id for which payment object has to be transferred

        Returns:
            Payment dict after getting transferred
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_id}/transfers"
        return self.post(url, data, **kwargs)

    def transfers(self, payment_id, data=None, **kwargs):
        """Fetch all transfer for given Payment Id.

        Args:
            payment_id : Id for which all the transfers has to be fetched

        Returns:
            A collection (dict) of transfers
            items : The key containing a list of 'transfer' entities
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_id}/transfers"
        return self.get(url, data, **kwargs)

    def bank_transfer(self, payment_id, data=None, **kwargs):
        """Bank Transfer Entity for given Payment.

        Args:
            payment_id : Id for which bank transfer entity has to be fetched

        Returns:
            Bank Transfer dict
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_id}/bank_transfer"
        return self.get(url, data, **kwargs)

    def upi_transfer(self, payment_id, data=None, **kwargs):
        """UPI Transfer Entity for given Payment.

        Args:
            payment_id : Id for which upi transfer entity has to be fetched

        Returns:
            UPI Transfer dict
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_id}/upi_transfer"
        return self.get(url, data, **kwargs)

    def refund(self, payment_id, amount=None, data=None, **kwargs):
        """Refund payment for given ID.

        Args:
            payment_id: ID of the payment to refund
            amount: (Optional) Amount to refund. If None, full refund is issued.
            data: (Optional) Additional data for the refund request

        Returns:
            Payment dict after refund
        """
        url = f"{self.base_url}/{payment_id}/refund"
        data = data or {}
        if amount is not None:
            data["amount"] = amount
        return self.post(url, data, **kwargs)

    def fetch_multiple_refund(self, payment_id, data=None, **kwargs):
        """Fetch multiple refunds for a payment.

        Returns:
            refunds dict
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_id}/refunds"
        return self.get(url, data, **kwargs)

    def fetch_refund_id(self, payment_id, refund_id, **kwargs):
        """Fetch a specific refund for a payment.

        Returns:
            Refund dict
        """
        url = f"{self.base_url}/{payment_id}/refunds/{refund_id}"
        return self.get(url, {}, **kwargs)

    def edit(self, payment_id, data=None, **kwargs):
        """Update the Payment.

        Args:
            data : Dictionary having keys using which order have to be edited
                'notes' : key value pair as notes

        Returns:
            Payment Dict which was edited
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_id}"
        return self.patch(url, data, **kwargs)

    def fetchCardDetails(self, payment_id, **kwargs):
        """Fetch Card Details of a Payment.

        Args:
            payment_id : Id for which payment objects has to be retrieved

        Returns:
            Payment dict for given Order Id
        """
        url = f"{self.base_url}/{payment_id}/card"
        return self.get(url, {}, **kwargs)

    def fetchDownTime(self, **kwargs):
        """Fetch Card Downtime Details.

        Returns:
            Payment dict for given Order Id
        """
        url = "{}/{}".format(self.base_url, "downtimes")
        return self.get(url, {}, **kwargs)

    def fetchDownTimeById(self, downtime_id, **kwargs):
        """Fetch Payment Downtime Details by ID.

        Args:
            downtime_id : Id for which downtime details have to be retrieved

        Returns:
            Payment dict for given downtime Id
        """
        url = f"{self.base_url}/downtimes/{downtime_id}"
        return self.get(url, {}, **kwargs)

    def createPaymentJson(self, data=None, **kwargs):
        """Create a Payment.

        Returns:
            Payment Dict which was created
        """
        if data is None:
            data = {}
        url = "{}/create/{}".format(self.base_url, "json")
        return self.post(url, data, **kwargs)

    def createRecurring(self, data=None, **kwargs):
        """Create Recurring Payments.

        Returns:
            Recurring Payments dict
        """
        if data is None:
            data = {}
        url = "{}/{}/recurring".format(self.base_url, "create")
        return self.post(url, data, **kwargs)

    def createUpi(self, data=None, **kwargs):
        """Initiate a payment.

        Returns:
            Payments dict
        """
        if data is None:
            data = {}
        url = "{}/create/{}".format(self.base_url, "upi")
        return self.post(url, data, **kwargs)

    def validateVpa(self, data=None, **kwargs):
        """Validate the VPA.

        Returns:
            Payments dict
        """
        if data is None:
            data = {}
        url = "{}/validate/{}".format(self.base_url, "vpa")
        return self.post(url, data, **kwargs)

    def fetchPaymentMethods(self, **kwargs):
        """Fetch payment methods.

        Returns:
            Payments dict
        """
        url = "/{}".format("methods")
        return self.get(url, {}, **kwargs)

    def otpGenerate(self, payment_id, data=None, **kwargs):
        """Generate an otp for payment.

        Args:
            payment_id : Id for which otp has to be generated

        Returns:
            Otp Dict which was created
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_id}/otp_generate"
        return self.post(url, data, **kwargs)

    def otpSubmit(self, payment_id, data=None, **kwargs):
        """Otp Submit.

        Args:
            payment_id : Id for which otp has to be submitted

        Returns:
            Otp Dict which was created
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_id}/otp/submit"
        return self.post(url, data, **kwargs)

    def otpResend(self, payment_id, data=None, **kwargs):
        """Otp Resend.

        Args:
            payment_id : Id for which otp has to be resent

        Returns:
            Otp Dict which was created
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{payment_id}/otp/resend"
        return self.post(url, data, **kwargs)
