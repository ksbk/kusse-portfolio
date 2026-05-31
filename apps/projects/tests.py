from typing import cast

from django.test import TestCase

from .models import Project, ProjectCategory, ProjectStatus


class ProjectModelTests(TestCase):
    def test_str_returns_title(self) -> None:
        project = Project(
            title="Portfolio Platform",
            slug="portfolio-platform",
            summary="Professional portfolio website project.",
            category=ProjectCategory.WEB,
            status=ProjectStatus.ACTIVE,
            role="Solo developer",
            tech_stack="Python, Django",
        )

        self.assertEqual(str(project), "Portfolio Platform")

    def test_project_can_be_created_with_minimum_required_fields(self) -> None:
        project = Project.objects.create(
            title="Projects App Scaffold",
            slug="projects-app-scaffold",
            summary="Initial dedicated projects app setup.",
            category=ProjectCategory.WEB,
            status=ProjectStatus.ACTIVE,
            role="Developer",
            tech_stack="Python, Django",
        )

        self.assertEqual(project.title, "Projects App Scaffold")
        self.assertEqual(Project.objects.count(), 1)

    def test_defaults_are_applied(self) -> None:
        project = Project.objects.create(
            title="Automation Utility",
            slug="automation-utility",
            summary="Small automation utility project.",
            category=ProjectCategory.AUTOMATION,
            status=ProjectStatus.EXPERIMENTAL,
            role="Developer",
            tech_stack="Python",
        )

        self.assertFalse(project.featured)
        self.assertEqual(project.display_order, 0)

    def test_model_meta_ordering(self) -> None:
        ordering = cast(list[str], Project._meta.ordering)
        self.assertEqual(ordering, ["display_order", "title"])

    def test_slug_field_is_unique(self) -> None:
        slug_field = Project._meta.get_field("slug")
        self.assertTrue(getattr(slug_field, "unique", False))
