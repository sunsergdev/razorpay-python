"""Utilities."""

# Standard library imports
import hashlib
import hmac

# Razorpay SDK local imports
from ..errors import SignatureVerificationError


class Utility:
    """Class that contains utility functions."""

    def __init__(self, client=None):
        self.client = client

    def verify_payment_signature(self, parameters):
        """Verify the signature of a payment request.

        This method checks if the signature generated during the payment
        matches the one received from Razorpay.

        Args:
            parameters (dict): A dictionary containing 'razorpay_order_id',
                'razorpay_payment_id', and 'razorpay_signature'.

        Returns:
            bool: True if the signature is valid, otherwise raises an error.
        """
        order_id = str(parameters["razorpay_order_id"])
        payment_id = str(parameters["razorpay_payment_id"])
        razorpay_signature = str(parameters["razorpay_signature"])

        msg = f"{order_id}|{payment_id}"

        secret = str(self.client.auth[1])

        return self.verify_signature(msg, razorpay_signature, secret)

    def verify_payment_link_signature(self, parameters):
        """Verify the signature for a Razorpay Payment Link.

        This method validates the signature sent by Razorpay for a payment
        link transaction using the relevant parameters.

        Args:
            parameters (dict): A dictionary containing 'razorpay_payment_id',
                'payment_link_id', 'payment_link_reference_id',
                'payment_link_status', and optionally 'secret'.

        Returns:
            bool: True if the signature is valid, False if required keys are missing.
        """
        if (
            "razorpay_payment_id" in parameters.keys()
            and "payment_link_reference_id" in parameters.keys()
            and "payment_link_status" in parameters.keys()
        ):
            payment_id = str(parameters["razorpay_payment_id"])
            payment_link_id = str(parameters["payment_link_id"])
            payment_link_reference_id = str(parameters["payment_link_reference_id"])
            payment_link_status = str(parameters["payment_link_status"])
            razorpay_signature = str(parameters["razorpay_signature"])
        else:
            return False

        msg = f"{payment_link_id}|{payment_link_reference_id}|{payment_link_status}|{payment_id}"

        secret = (
            str(parameters["secret"]) if "secret" in parameters.keys() else str(self.client.auth[1])
        )

        return self.verify_signature(msg, razorpay_signature, secret)

    def verify_subscription_payment_signature(self, parameters):
        """Verify subscription payment signature.

        To consider the payment as successful and subscription as authorized
        after the signature has been successfully verified
        """
        subscription_id = str(parameters["razorpay_subscription_id"])
        payment_id = str(parameters["razorpay_payment_id"])
        razorpay_signature = str(parameters["razorpay_signature"])

        msg = f"{payment_id}|{subscription_id}"

        secret = (
            str(parameters["secret"]) if "secret" in parameters.keys() else str(self.client.auth[1])
        )

        return self.verify_signature(msg, razorpay_signature, secret)

    def verify_webhook_signature(self, body, signature, secret):
        """Verify the webhook signature using the provided secret.

        Args:
            body (str): The raw request body from the webhook.
            signature (str): The signature sent in the `X-Razorpay-Signature` header.
            secret (str): The webhook secret configured in Razorpay dashboard.

        Returns:
            bool: True if the signature is valid, else raises an exception.
        """
        return self.verify_signature(body, signature, secret)

    def verify_signature(self, body, signature, key):
        """Verify a Razorpay signature using HMAC SHA256.

        Args:
            body (str): The message body used to generate the signature.
            signature (str): The expected HMAC signature to verify.
            key (str): The secret key used to generate the signature.

        Raises:
            SignatureVerificationError: If the generated signature does not match the provided one.

        Returns:
            bool: True if the signature is valid.
        """
        key = bytes(key, "utf-8")
        body = bytes(body, "utf-8")

        dig = hmac.new(key=key, msg=body, digestmod=hashlib.sha256)

        generated_signature = dig.hexdigest()

        result = hmac.compare_digest(generated_signature, signature)

        if not result:
            msg = "Razorpay Signature Verification Failed"
            raise SignatureVerificationError(msg)
        return result

    # Taken from Django Source Code
    # Used in python version < 2.7.7
    # As hmac.compare_digest is not present in prev versions
    def compare_string(self, expected_str, actual_str):
        """Return True if the two strings are equal, False otherwise.

        The time taken is independent of the number of characters that match
        For the sake of simplicity, this function executes in constant time only
        when the two strings have the same length. It short-circuits when they
        have different lengths
        """
        if len(expected_str) != len(actual_str):
            return False
        result = 0
        for x, y in zip(expected_str, actual_str, strict=False):
            result |= ord(x) ^ ord(y)
        return result == 0
