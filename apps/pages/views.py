"""Placeholder views for the initial Django scaffold."""
from typing import Any

from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["homepage"] = {
            "eyebrow": _("Research-trained software developer"),
            "title": _(
                "I build practical software with a researcher's attention "
                "to evidence, clarity, and real-world constraints."
            ),
            "description": _(
                "This portfolio brings together my work across Python, data, "
                "applied AI, Django, full-stack web development, research software, "
                "and technical writing."
            ),
            "primary_cta": _("View selected work"),
            "secondary_cta": _("Contact me"),
        }
        return context