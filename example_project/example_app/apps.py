from django.apps import AppConfig
from django.conf import settings
from django.utils.autoreload import autoreload_started


def schema_watchdog(sender, **kwargs):
    """This allows us to add all `*.graphql` files to django's autoreloader,
    saving us of having to go through the hassle of restarting django's
    development server everytime we make a change to our graphql schema. Don't
    forget to add lines 17 and 18 too."""
    sender.watch_dir(settings.BASE_DIR, "**/*.graphql")


class ExampleAppConfig(AppConfig):
    name = "example_app"

    def ready(self):
        autoreload_started.connect(schema_watchdog)
