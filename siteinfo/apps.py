from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SiteinfoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "siteinfo"
    verbose_name = _("تنظیمات وب اپلیکیشن")
