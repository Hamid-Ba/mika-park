from django.contrib import admin

from agent import models


class BranchInline(admin.TabularInline):
    model = models.Agent_Branch
    extra = 1


class AgentAdmin(admin.ModelAdmin):
    """Agent Admin Model"""

    list_display = ["id"]
    list_display_links = ["id"]
    # list_editable = ["name"]

    inlines = [BranchInline]


admin.site.register(models.Agent, AgentAdmin)
