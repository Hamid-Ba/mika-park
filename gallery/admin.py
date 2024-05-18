from django.contrib import admin

from gallery import models

# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    """Gallery Admin Model"""

    list_display = ["id", "title", "is_show", "image_path"]
    list_display_links = ["id", "title"]
    sortable_by = ["title"]
    search_fields = ["title"]
    list_filter = ["is_show"]
    list_editable = ["is_show"]

    def image_path(self, obj):
        return obj.image.path


admin.site.register(models.Gallery, GalleryAdmin)
