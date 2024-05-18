from django.contrib import admin

from jalali_date.admin import (
    ModelAdminJalaliMixin,
)

from contactus import models


class MessageAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    """Message Admin Model"""

    list_display = ["id", "full_name", "phone", "create_date"]
    list_display_links = ["id", "full_name", "phone"]


class AddressAdmin(admin.ModelAdmin):
    """Address Admin Model"""

    list_display = ["id", "address"]
    list_display_links = ["id"]
    list_editable = ["address"]


class PhoneAdmin(admin.ModelAdmin):
    """Phone Admin Model"""

    list_display = ["id", "phone"]
    list_display_links = ["id"]
    list_editable = ["phone"]


class EmailAdmin(admin.ModelAdmin):
    """Email Admin Model"""

    list_display = ["id", "email"]
    list_display_links = ["id"]
    list_editable = ["email"]


admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.Phone, PhoneAdmin)
admin.site.register(models.Email, EmailAdmin)
