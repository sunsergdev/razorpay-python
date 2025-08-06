"""RegistrationLink resource."""

# Razorpay SDK local imports
from ..constants.url import URL
from .base import Resource


class RegistrationLink(Resource):
    """Resource class for handling Razorpay RegistrationLink APIs."""

    def __init__(self, client=None):
        super().__init__(client)
        self.base_url = URL.V1 + URL.REGISTRATION_LINK_URL

    def create(self, data=None, **kwargs):
        """Create a Registration Link.

        Args:
            customer : Details of the customer to whom the registration link will be sent.
            type* : In this case the value is link.
            currency* : Currency used in Order
            amount* : Amount of Order
            description : The count may not be greater than 100.
            subscription_registration : Details of the authorization payment.
            notes : A key-value pair

        Returns:
            {"success": true}
        """
        if data is None:
            data = {}
        url = "{}/{}".format(self.base_url, "auth_links")
        return self.post(url, data, **kwargs)
