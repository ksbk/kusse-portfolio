from typing import TYPE_CHECKING

from django.contrib import admin

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
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "summary",
                    "category",
                    "status",
                )
            },
        ),
        (
            "Project details",
            {
                "fields": (
                    "problem_context",
                    "technical_approach",
                    "role",
                    "tech_stack",
                )
            },
        ),
        (
            "Evidence links",
            {
                "fields": (
                    "repository_url",
                    "live_url",
                    "documentation_url",
                )
            },
        ),
        (
            "Visual evidence",
            {"fields": ("image", "image_alt_text")},
        ),
        (
            "Presentation",
            {
                "fields": (
                    "featured",
                    "display_order",
                )
            },
        ),
    )
    ordering = ("display_order", "title")
