from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContactusConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "contactus"
    verbose_name = "ارتباط با ما"
