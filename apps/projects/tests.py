from typing import cast

from io import StringIO

from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

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


class ProjectIndexViewTests(TestCase):
    def test_projects_index_renders_empty_state(self) -> None:
        response = self.client.get(reverse("projects:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Projects will be added soon")
        self.assertTemplateUsed(response, "projects/index.html")

    def test_projects_index_renders_project_records(self) -> None:
        Project.objects.create(
            title="Portfolio Platform",
            slug="portfolio-platform",
            summary="Professional portfolio website project.",
            category=ProjectCategory.WEB,
            status=ProjectStatus.ACTIVE,
            role="Solo developer",
            tech_stack="Python, Django",
        )

        response = self.client.get(reverse("projects:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Portfolio Platform")
        self.assertContains(response, "Professional portfolio website project.")
        self.assertContains(response, "Python, Django")

    def test_projects_index_renders_available_links(self) -> None:
        Project.objects.create(
            title="Public Project",
            slug="public-project",
            summary="Project with supporting links.",
            category=ProjectCategory.WEB,
            status=ProjectStatus.COMPLETED,
            role="Developer",
            tech_stack="Python, Django",
            repository_url="https://github.com/example/project",
            live_url="https://example.com",
            documentation_url="https://docs.example.com",
        )

        response = self.client.get(reverse("projects:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Repository")
        self.assertContains(response, "Live site")
        self.assertContains(response, "Documentation")
        self.assertContains(response, "https://github.com/example/project")
        self.assertContains(response, "https://example.com")
        self.assertContains(response, "https://docs.example.com")
        
        
        
class ProjectDetailViewTests(TestCase):
    def test_project_detail_renders_project_record(self) -> None:
        project = Project.objects.create(
            title="Portfolio Platform",
            slug="portfolio-platform",
            summary="Professional portfolio website project.",
            category=ProjectCategory.WEB,
            status=ProjectStatus.ACTIVE,
            role="Solo developer",
            tech_stack="Python, Django",
            problem_context="A need for a structured professional portfolio.",
            technical_approach="Built with Django apps, templates, and tests.",
            repository_url="https://github.com/example/portfolio-platform",
        )

        response = self.client.get(reverse("projects:detail", args=[project.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects/detail.html")
        self.assertContains(response, "Portfolio Platform")
        self.assertContains(response, "Professional portfolio website project.")
        self.assertContains(response, "Solo developer")
        self.assertContains(response, "Python, Django")
        self.assertContains(response, "A need for a structured professional portfolio.")
        self.assertContains(response, "Built with Django apps, templates, and tests.")
        self.assertContains(response, "Repository")

    def test_project_detail_returns_404_for_missing_slug(self) -> None:
        response = self.client.get(reverse("projects:detail", args=["missing-project"]))

        self.assertEqual(response.status_code, 404)

    def test_projects_index_links_to_detail_page(self) -> None:
        project = Project.objects.create(
            title="Linked Project",
            slug="linked-project",
            summary="Project shown on the index page.",
            category=ProjectCategory.WEB,
            status=ProjectStatus.COMPLETED,
            role="Developer",
            tech_stack="Python, Django",
        )

        response = self.client.get(reverse("projects:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse("projects:detail", args=[project.slug]))
        
class SeedProjectsCommandTests(TestCase):
    def test_seed_projects_creates_initial_project_records(self) -> None:
        output = StringIO()

        call_command("seed_projects", stdout=output)

        self.assertEqual(Project.objects.count(), 5)
        self.assertTrue(
            Project.objects.filter(
                slug="traffic-sign-image-classifier",
                title="Traffic Sign Image Classifier",
            ).exists()
        )
        self.assertIn("5 created, 0 updated", output.getvalue())

    def test_seed_projects_is_safe_to_rerun(self) -> None:
        first_output = StringIO()
        second_output = StringIO()

        call_command("seed_projects", stdout=first_output)
        call_command("seed_projects", stdout=second_output)

        self.assertEqual(Project.objects.count(), 5)
        self.assertIn("0 created, 5 updated", second_output.getvalue())