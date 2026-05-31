from django.contrib import admin
from typing import TYPE_CHECKING

from .models import Project


if TYPE_CHECKING:
    ProjectAdminBase = admin.ModelAdmin[Project]
else:
    ProjectAdminBase = admin.ModelAdmin


@admin.register(Project)
class ProjectAdmin(ProjectAdminBase):
    list_display = ("title", "category", "status", "featured", "display_order", "updated_at")
    list_filter = ("category", "status", "featured")
    search_fields = ("title", "summary", "tech_stack")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("display_order", "title")
