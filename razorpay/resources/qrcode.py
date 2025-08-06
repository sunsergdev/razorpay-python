"""QrCode resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Qrcode(Resource):
    """Resource class for handling Razorpay Qrcode APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.QRCODE_URL

    def fetch(self, qrcode_id, data=None, **kwargs):
        """Fetch a Qr code.

        Args:
            qrcode_id : Id for which Qrcode object has to be retrieved

        Returns:
            Qrcode dict for given qrcode id
        """
        if data is None:
            data = {}
        return super().fetch(qrcode_id, data, **kwargs)

    def create(self, data=None, **kwargs):
        """Create a QR Code.

        Returns:
            QrCode Dict which was created
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.post(url, data, **kwargs)

    def all(self, data=None, **kwargs):
        """Fetch all Qr Codes.

        Returns:
            Qrcode dict
        """
        if data is None:
            data = {}
        return super().all(data, **kwargs)

    def fetch_all_payments(self, qrcode_id, data=None, **kwargs):
        """Fetch Payments for a QR Code.

        Args:
            qrcode_id : Id for which Qrcode payments have to be fetched

        Returns:
            Qrcode payment dict
        """
        if data is None:
            data = {}
        url = f"{self.base_url}/{qrcode_id}/payments"
        return self.get(url, data, **kwargs)

    def close(self, qrcode_id, **kwargs):
        """Close a QR Code.

        Args:
            qrcode_id : Id for which Qrcode has to be closed

        Returns:
            Qrcode Dict which was closed
        """
        url = f"{self.base_url}/{qrcode_id}/close"
        return self.post(url, {}, **kwargs)
