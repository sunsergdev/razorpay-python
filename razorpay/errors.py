"""Errors raised by razorpay python SDK."""


class BadRequestError(Exception):
    """Exception raised for invalid or malformed requests."""

    def __init__(self, message=None, *args, **kwargs):
        super().__init__(message)


class GatewayError(Exception):
    """Exception raised when a gateway (e.g., payment provider) error occurs."""

    def __init__(self, message=None, *args, **kwargs):
        super().__init__(message)


class ServerError(Exception):
    """Exception raised when a server-side error occurs."""

    def __init__(self, message=None, *args, **kwargs):
        super().__init__(message)


class SignatureVerificationError(Exception):
    """Exception raised when signature verification fails."""

    def __init__(self, message=None, *args, **kwargs):
        super().__init__(message)
