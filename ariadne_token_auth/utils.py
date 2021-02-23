from django.conf import settings


def get_settings_or_default(setting_name):
    specific_settings = getattr(
        settings, "ARIADNE_TOKEN_AUTH", {"TOKEN_NAME": "Token", "TOKEN_LENGTH": 35}
    )
    return specific_settings.get(setting_name)


TOKEN_NAME = get_settings_or_default("TOKEN_NAME")
TOKEN_LENGTH = get_settings_or_default("TOKEN_LENGTH")
