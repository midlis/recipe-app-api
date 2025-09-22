"""App configuration."""

from django.apps import AppConfig


class UserConfig(AppConfig):
    """User app config."""

    default_auto_field = (  # pyright: ignore[reportUnannotatedClassAttribute]
        'django.db.models.BigAutoField'
    )
    name: str = 'user'
