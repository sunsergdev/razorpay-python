"""Document resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class Document(Resource):
    """Resource class for handling Razorpay Document APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.DOCUMENT

    def create(self, data=None, **kwargs):
        """Create a Document.

        Returns:
            Dictionary of document
        """
        if data is None:
            data = {}
        url = self.base_url
        return self.file(url, data, **kwargs)

    def fetch(self, dispute_id, data=None, **kwargs):
        """Fetch Document.

        Args:
            dispute_id : Id for which document object has to be retrieved

        Returns:
            Dictionary of document
        """
        if data is None:
            data = {}
        return super().fetch(dispute_id, data, **kwargs)
