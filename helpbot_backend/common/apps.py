from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "helpbot_backend.common"
    verbose_name = _("Magage Project")

    def ready(self):
        try:
            import helpbot_backend.common.signals  # noqa: F401
        except ImportError:
            pass
