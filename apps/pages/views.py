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
            "eyebrow": _("Software developer with a research background"),
            "title": _(
                "I build software with attention to clarity, evidence, "
                "and real-world constraints."
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
            "title": _("Research background, software direction, and technical work."),
            "description": _(
                "I am building a professional path across "
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

class ResearchView(TemplateView):
    """Render the portfolio research page."""

    template_name = "pages/research.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["research_page"] = {
            "eyebrow": _("Research"),
            "title": _("Research training applied to technical problem-solving."),
            "description": _(
                "My research background shapes how I approach software: define the problem clearly, "
                "study constraints, evaluate evidence, and communicate results honestly."
            ),
            "focus_areas": [
                {
                    "title": _("Scientific problem-solving"),
                    "description": _(
                        "Experience across physics, computer science, and chemistry gives me a broad "
                        "foundation for analyzing complex technical systems."
                    ),
                },
                {
                    "title": _("Research software"),
                    "description": _(
                        "I am interested in software that supports reproducible workflows, data analysis, "
                        "simulation, documentation, and scientific communication."
                    ),
                },
                {
                    "title": _("Applied AI and healthcare technology"),
                    "description": _(
                        "My long-term direction includes practical, evidence-aware technology for health, "
                        "education, and decision support without overstating what software can do."
                    ),
                },
            ],
        }
        return context

class ProjectsView(TemplateView):
    """Render the portfolio projects page shell."""

    template_name = "pages/projects.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["projects_page"] = {
            "eyebrow": _("Projects"),
            "title": _("Selected software, research, and technical work."),
            "description": _(
                "This page will become a structured portfolio of selected projects. "
                "For now, it introduces the main categories of work that will be expanded "
                "with stronger evidence, links, and case studies."
            ),
            "categories": [
                {
                    "title": _("Flagship projects"),
                    "description": _(
                        "Larger, higher-evidence projects that best represent my current technical direction."
                    ),
                },
                {
                    "title": _("Research software"),
                    "description": _(
                        "Tools, workflows, simulations, and technical work connected to research practice."
                    ),
                },
                {
                    "title": _("Applied Python and data"),
                    "description": _(
                        "Practical projects involving Python, automation, data handling, and applied AI concepts."
                    ),
                },
                {
                    "title": _("Full-stack and backend engineering"),
                    "description": _(
                        "Web applications and backend systems built with attention to structure, maintainability, and deployment."
                    ),
                },
                {
                    "title": _("Engineering process and documentation"),
                    "description": _(
                        "Work that demonstrates planning, documentation, testing, technical communication, and reviewable decisions."
                    ),
                },
            ],
        }
        return context

class CVView(TemplateView):
    """Render the portfolio CV page."""

    template_name = "pages/cv.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["cv_page"] = {
            "eyebrow": _("CV"),
            "title": _("Professional profile and technical background"),
            "description": _(
                "A concise web CV summarizing my research training, technical skills, "
                "software direction, and selected areas of work."
            ),
            "summary": _(
                "Software developer with research training across physics, "
                "computer science, and chemistry. I am focused on Python, Django, data-informed "
                "applications, research software, and clear technical communication."
            ),
            "skill_groups": [
                {
                    "title": _("Software development"),
                    "items": [_("Python"), _("Django"), _("HTML"), _("CSS"), _("JavaScript"), _("SQL")],
                },
                {
                    "title": _("Research and data"),
                    "items": [_("Scientific reasoning"), _("Data analysis"), _("Applied AI concepts"), _("Technical writing")],
                },
                {
                    "title": _("Engineering practice"),
                    "items": [_("Git"), _("GitHub workflow"), _("Documentation"), _("Testing"), _("Incremental delivery")],
                },
            ],
            "sections": [
                {
                    "title": _("Research background"),
                    "description": _(
                        "Academic training across science and computing, with experience in structured "
                        "problem-solving, experimentation, analysis, and communication."
                    ),
                },
                {
                    "title": _("Software direction"),
                    "description": _(
                        "Current work focuses on professional web development, Django applications, "
                        "portfolio systems, research software, and practical applied AI/data tools."
                    ),
                },
                {
                    "title": _("Selected work"),
                    "description": _(
                        "This portfolio itself is being built as public evidence of planning, implementation, "
                        "documentation, typed configuration, GitHub workflow, and incremental delivery."
                    ),
                },
            ],
        }
        return context
    
class ContactView(TemplateView):
    """Render the portfolio contact page."""

    template_name = "pages/contact.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["contact_page"] = {
            "eyebrow": _("Contact"),
            "title": _("Start a focused conversation."),
            "description": _(
                "I am open to conversations about research software, Django development, "
                "technical documentation, portfolio systems, and practical applied software work."
            ),
            "contact_methods": [
                {
                    "title": _("Email"),
                    "description": _("Best for direct professional inquiries and project conversations."),
                    "label": _("Email me"),
                    "url": "mailto:kbersha@gmail.com",
                },
                {
                    "title": _("GitHub"),
                    "description": _("Review public code, project history, documentation, and development workflow."),
                    "label": _("View GitHub"),
                    "url": "https://github.com/ksbk",
                },
            ],
            "note_title": _("Before contacting me"),
            "note": _(
                "The most useful messages include the problem, context, timeline, and what kind "
                "of technical help or collaboration you are considering."
            ),
        }
        return context