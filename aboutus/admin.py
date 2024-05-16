from django.contrib import admin

from aboutus import models


class AboutUsAdmin(admin.ModelAdmin):
    """AboutUs Admin Model"""

    list_display = ["id", "title"]
    list_display_links = ["id", "title"]


class AboutUsExtensionAdmin(admin.ModelAdmin):
    """AboutUsExtension Admin Model"""

    list_display = ["id", "main_title", "title"]
    list_display_links = ["id"]
    list_editable = ["main_title", "title"]


admin.site.register(models.AboutUs, AboutUsAdmin)
admin.site.register(models.AboutUsExtension, AboutUsExtensionAdmin)
