from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ManageProjectConfig(AppConfig):
    name = "helpbot_backend.manage_project"
    verbose_name = _("Magage Project")

    def ready(self):
        try:
            import helpbot_backend.manage_project.signals  # noqa: F401
        except ImportError:
            pass
