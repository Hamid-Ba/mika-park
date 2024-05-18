from django.contrib import admin

from project import models


class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title"]
    list_display_links = ["id", "title"]

class SpecificationInline(admin.TabularInline):
    model = models.Project_Specification
    extra = 1
    
class PropertyInline(admin.TabularInline):
    model = models.Project_Property
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    """Project Admin Model"""
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]
    filter_horizontal = ("gallery", "features",)
    inlines = [SpecificationInline, PropertyInline]

admin.site.register(models.Feature, FeatureAdmin)
admin.site.register(models.Project, ProjectAdmin)