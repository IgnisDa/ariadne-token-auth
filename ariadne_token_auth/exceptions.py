from django.utils.translation import ugettext_lazy as _


class AuthTokenTokenError(Exception):
    default_message = None

    def __init__(self, message=None):
        if message is None:
            message = self.default_message

        super(AuthTokenTokenError, self).__init__(message)


class PermissionDenied(AuthTokenTokenError):
    default_message = _("You do not have permission to perform this action")
