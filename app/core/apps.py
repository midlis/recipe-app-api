"""App configuration."""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configuration class for core."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
