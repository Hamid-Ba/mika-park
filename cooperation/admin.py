from django.contrib import admin

from cooperation import models

class CooperationTypeAdmin(admin.ModelAdmin):
    """Cooperation Type Admin"""
    list_display = ["id", "title"]
    list_display_links = ["id"]
    list_editable = ["title"]


class CooperationRequestAdmin(admin.ModelAdmin):
    """Cooperation Request Admin"""
    list_display = ["id", "first_name", "last_name", "phone", "email", "type"]
    list_display_links = ["id", "first_name", "last_name"]
    list_filter = ["type"]
    search_fields = ["first_name", "last_name", "phone", "email"]


admin.site.register(models.CooperationType, CooperationTypeAdmin)
admin.site.register(models.CooperationRequest, CooperationRequestAdmin)