"""Views for structured project portfolio pages."""

from typing import TYPE_CHECKING, Any

from django.views.generic import DetailView, TemplateView

from .models import Project


if TYPE_CHECKING:
    ProjectDetailViewBase = DetailView[Project]
else:
    ProjectDetailViewBase = DetailView


class ProjectIndexView(TemplateView):
    """Render the structured projects index page."""

    template_name = "projects/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["projects_index"] = {
            "eyebrow": "Projects",
            "title": "Technical projects",
            "description": (
                "Selected projects from my computer science, AI, Python, database, "
                "and systems programming practice, organized to show the problems "
                "solved, tools used, and technical decisions made."
            ),
        }
        context["projects"] = Project.objects.all()
        return context


class ProjectDetailView(ProjectDetailViewBase):
    """Render the structured projects detail page."""

    model = Project
    template_name = "projects/detail.html"
    context_object_name = "project"