from django.apps import AppConfig
from django.conf import settings
from django.utils.autoreload import autoreload_started


def schema_watchdog(sender, **kwargs):
    sender.watch_dir(settings.BASE_DIR, "**/*.graphql")


class ExampleAppConfig(AppConfig):
    name = "example_app"

    def ready(self):
        autoreload_started.connect(schema_watchdog)
