"""Views for public portfolio pages."""

from typing import Any

from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Render the portfolio homepage."""

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
            "featured_work": [
                {
                    "title": _("Django portfolio platform"),
                    "description": _(
                        "A professional portfolio system built with Django, structured "
                        "documentation, typed settings, and a clean public development workflow."
                    ),
                    "label": _("Full-stack web development"),
                },
                {
                    "title": _("Research and technical writing"),
                    "description": _(
                        "Scientific and technical work shaped by research training, "
                        "evidence-based reasoning, and careful explanation."
                    ),
                    "label": _("Research communication"),
                },
                {
                    "title": _("Applied Python and data projects"),
                    "description": _(
                        "Practical software experiments using Python, automation, data handling, "
                        "and applied AI concepts."
                    ),
                    "label": _("Python and data"),
                },
            ],
            "identity_points": [
                _("Research background in science and computational problem-solving."),
                _("Software development focused on clarity, maintainability, and practical use."),
                _("Interest in applied AI, healthcare technology, and research software."),
            ],
            "skills": [
                _("Python"),
                _("Django"),
                _("HTML"),
                _("CSS"),
                _("JavaScript"),
                _("SQL"),
                _("Data analysis"),
                _("Technical writing"),
            ],
            "engagement_options": [
                {
                    "title": _("Review my work"),
                    "description": _("Explore selected projects, code, documentation, and development decisions."),
                },
                {
                    "title": _("Understand my background"),
                    "description": _("Read about my research training, technical direction, and professional story."),
                },
                {
                    "title": _("Start a conversation"),
                    "description": _("Contact me about research software, web development, or applied technical work."),
                },
            ],
            "contact_title": _("Interested in working together?"),
            "contact_description": _(
                "I am open to conversations around research software, Django development, "
                "technical documentation, and practical software projects."
            ),
        }
        return context

class AboutView(TemplateView):
    """Render the portfolio about page."""

    template_name = "pages/about.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["about_page"] = {
            "eyebrow": _("About"),
            "title": _("Research background, software direction, and practical technical work."),
            "description": _(
                "I am a research-trained technologist building a professional path across "
                "software development, applied data work, research communication, and practical "
                "tools for real-world problems."
            ),
            "sections": [
                {
                    "title": _("Research foundation"),
                    "description": _(
                        "My background in physics, computer science, and chemistry shaped how I "
                        "approach problems: define the question carefully, examine evidence, and "
                        "communicate uncertainty honestly."
                    ),
                },
                {
                    "title": _("Software direction"),
                    "description": _(
                        "I am focused on Python, Django, data-informed applications, full-stack web "
                        "development, and research software that is clear, maintainable, and useful."
                    ),
                },
                {
                    "title": _("Working style"),
                    "description": _(
                        "I value readable code, structured documentation, careful naming, incremental "
                        "delivery, and transparent engineering decisions that others can review."
                    ),
                },
            ],
        }
        return context