from django.contrib import admin

from siteinfo import models


class HomeHeaderAdmin(admin.ModelAdmin):
    """Home Header Admin Model"""

    list_display = ["id", "heading"]
    list_display_links = ["id", "heading"]


class ServiceAdmin(admin.ModelAdmin):
    """Service Admin Model"""

    list_display = ["id", "title"]
    list_display_links = ["id", "title"]


class FeatureAdmin(admin.ModelAdmin):
    """Feature Admin Model"""

    list_display = ["id", "title"]
    list_display_links = ["id", "title"]


class FooterAdmin(admin.ModelAdmin):
    """Footer Admin Model"""

    list_display = ["id", "title"]
    list_display_links = ["id", "title"]


class FooterLinkAdmin(admin.ModelAdmin):
    """FooterLink Admin Model"""

    list_display = ["id", "title", "footer_link_type", "link"]
    list_display_links = ["id", "title"]
    list_editable = ["link", "footer_link_type"]


class CommunicationAdmin(admin.ModelAdmin):
    """Communication Admin Model"""

    list_display = ["id", "title"]
    list_display_links = ["id", "title"]


admin.site.register(models.HomeHeader, HomeHeaderAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Feature, FeatureAdmin)
admin.site.register(models.Footer, FooterAdmin)
admin.site.register(models.FooterLink, FooterLinkAdmin)
admin.site.register(models.Communication, CommunicationAdmin)
