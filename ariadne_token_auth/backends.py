from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

from django_tokens import models

User = get_user_model()


class AuthTokenBackend(BaseBackend):
    """ A custom backend to authenticate using tokens. """

    def authenticate(self, request, token_string=None, *args, **kwargs):
        # Check the username/password and return a user.
        try:
            return models.AuthToken.objects.get(token_string=token_string).user
        except models.AuthToken.DoesNotExist:
            return None
