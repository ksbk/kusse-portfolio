from django.db import models


class ProjectCategory(models.TextChoices):
    WEB = "web", "Web"
    RESEARCH_SOFTWARE = "research_software", "Research software"
    AI_DATA = "ai_data", "AI and data"
    AUTOMATION = "automation", "Automation"
    INFRASTRUCTURE = "infrastructure", "Infrastructure"
    OTHER = "other", "Other"


class ProjectStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    COMPLETED = "completed", "Completed"
    PAUSED = "paused", "Paused"
    ARCHIVED = "archived", "Archived"
    EXPERIMENTAL = "experimental", "Experimental"


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    category = models.CharField(max_length=32, choices=ProjectCategory.choices)
    status = models.CharField(max_length=16, choices=ProjectStatus.choices)
    problem_context = models.TextField(blank=True)
    technical_approach = models.TextField(blank=True)
    role = models.CharField(max_length=255)
    tech_stack = models.TextField(help_text="Comma-separated technologies or short stack description.")
    repository_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    documentation_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "title"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self) -> str:
        return self.title
