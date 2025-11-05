from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


def full_details_exception_handler(var_0, var_1):
    """
    This overrides the default exception handler to
    include the human-readable message AND the error code
    so that clients can respond programmatically.
    """
    if isinstance(var_0, APIException):
        var_0.detail = var_0.get_full_details()

    return exception_handler(var_0, var_1)
