class AioDevisionException(Exception):
    """The Base exceptions to all other exceptions."""

class UndefinedLibraryError(AioDevisionException):
    """An Exception when you defined a undefined lib in RTFS endpoint."""


class TokenRequired(AioDevisionException):
    """An Exception when you are trying to access an endpoint that requires a token."""


class InvalidImage(AioDevisionException):
    """An Exception when you provided an invalid image to OCR and/or CDN."""


class InternalServerError(AioDevisionException):
    """An Exception when an unknown error happens. Go join x and Scream at IAmTomahawkx#1000."""


class InvalidDocumentation(AioDevisionException):
    """You provided an invalid documentation to the RTFM endpoint."""


class InvalidData(AioDevisionException):
    """You provided an invalid data in a request you made."""


class NotFound(AioDevisionException):
    """The URL provided was Not Found."""

    
class MaxRetryReached(AioDevisionException):
    """Max retries reached for a request. This can be changed using Client.retry."""
