"""Baseline route and template tests for public portfolio pages."""

from django.test import SimpleTestCase
from django.urls import reverse


class PageRouteTests(SimpleTestCase):
    """Verify public portfolio pages render successfully."""

    def test_homepage_renders_expected_template(self) -> None:
        response = self.client.get(reverse("pages:home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")

    def test_about_page_renders_expected_template(self) -> None:
        response = self.client.get(reverse("pages:about"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")

    def test_research_page_renders_expected_template(self) -> None:
        response = self.client.get(reverse("pages:research"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/research.html")

    def test_projects_page_renders_expected_template(self) -> None:
        response = self.client.get(reverse("pages:projects"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/projects.html")

    def test_cv_page_renders_expected_template(self) -> None:
        response = self.client.get(reverse("pages:cv"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/cv.html")

    def test_contact_page_renders_expected_template(self) -> None:
        response = self.client.get(reverse("pages:contact"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/contact.html")