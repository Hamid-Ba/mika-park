from django.contrib import admin
from new import models
from jalali_date.admin import (
    ModelAdminJalaliMixin,
)


class NewAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ("id", "title", "publish_date")
    list_display_links = ("id", "title")
    search_fields = ("title", "short_desc", "desc")


class NewsletterMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "create_date")
    list_display_links = ("id", "phone")
    search_fields = ("phone",)


admin.site.register(models.New, NewAdmin)
admin.site.register(models.NewsletterMember, NewsletterMemberAdmin)
