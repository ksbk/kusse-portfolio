"""Views for structured project portfolio pages."""

from typing import Any

from django.views.generic import TemplateView


class ProjectIndexView(TemplateView):
    """Render the structured projects index page."""

    template_name = "projects/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["projects_index"] = {
            "eyebrow": "Projects",
            "title": "Technical projects",
            "description": (
                "A structured overview of selected projects, technical work, "
                "and implementation experience."
            ),
        }
        return context