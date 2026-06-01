"""Seed initial project records for the portfolio."""

from typing import Any

from django.core.management.base import BaseCommand

from apps.projects.models import Project, ProjectCategory, ProjectStatus

PROJECT_RECORDS: list[dict[str, Any]] = [
    {
        "title": "Traffic Sign Image Classifier",
        "slug": "traffic-sign-image-classifier",
        "summary": (
            "An image classification model trained to recognize traffic signs "
            "using a neural network pipeline."
        ),
        "category": ProjectCategory.AI_DATA,
        "status": ProjectStatus.COMPLETED,
        "role": "Built and evaluated the image classification model",
        "tech_stack": (
            "Python, TensorFlow/Keras, neural networks, computer vision"
        ),
        "problem_context": (
            "Computer vision systems require reliable data preprocessing, model "
            "design, training, validation, and performance evaluation. This "
            "project focused on building and evaluating a practical image "
            "classification workflow."
        ),
        "technical_approach": (
            "Prepared image data, built and trained a neural network classifier, "
            "evaluated model behavior, and iterated on architecture choices to "
            "improve classification performance."
        ),
        "featured": True,
        "display_order": 10,
    },
    {
        "title": "AI Search and Reasoning Systems",
        "slug": "ai-search-and-reasoning-systems",
        "summary": (
            "A collection of AI systems implementing search, game decision-making, "
            "logical inference, ranking, uncertainty, and constraint-solving "
            "techniques."
        ),
        "category": ProjectCategory.AI_DATA,
        "status": ProjectStatus.COMPLETED,
        "role": "Implemented search, reasoning, and decision-making algorithms",
        "tech_stack": (
            "Python, graph search, minimax, logic, probability, constraint "
            "satisfaction"
        ),
        "problem_context": (
            "Many intelligent systems rely on searching large state spaces, "
            "reasoning under uncertainty, ranking information, or choosing "
            "actions based on available evidence."
        ),
        "technical_approach": (
            "Implemented graph search, adversarial search, propositional logic, "
            "probabilistic reasoning, PageRank-style ranking, constraint "
            "satisfaction, and optimization techniques across multiple focused "
            "AI implementations."
        ),
        "featured": True,
        "display_order": 20,
    },
    {
        "title": "Relational Data Modeling and SQL Analysis",
        "slug": "relational-data-modeling-and-sql-analysis",
        "summary": (
            "A structured database project demonstrating relational modeling, "
            "querying, views, and optimization."
        ),
        "category": ProjectCategory.AI_DATA,
        "status": ProjectStatus.COMPLETED,
        "role": "Designed queries and relational database structures",
        "tech_stack": (
            "SQL, SQLite, relational modeling, joins, views, indexes, query "
            "optimization"
        ),
        "problem_context": (
            "Reliable applications depend on well-designed data models, "
            "normalized relationships, efficient queries, and maintainable "
            "database structures."
        ),
        "technical_approach": (
            "Designed relational schemas, wrote SQL queries, used joins and views "
            "to extract information, and applied indexing and optimization "
            "concepts for better query performance."
        ),
        "featured": True,
        "display_order": 30,
    },
    {
        "title": "Python Automation and Data Processing Toolkit",
        "slug": "python-automation-and-data-processing-toolkit",
        "summary": (
            "A collection of Python programs demonstrating data processing, input "
            "validation, file handling, testing, regular expressions, and "
            "object-oriented design."
        ),
        "category": ProjectCategory.AUTOMATION,
        "status": ProjectStatus.COMPLETED,
        "role": (
            "Built small Python tools for validation, parsing, testing, and data "
            "handling"
        ),
        "tech_stack": (
            "Python, pytest, file I/O, regular expressions, OOP, CLI scripting"
        ),
        "problem_context": (
            "Many practical software tasks require reliable scripts that parse "
            "data, validate input, transform files, and automate repetitive "
            "workflows."
        ),
        "technical_approach": (
            "Implemented Python scripts and modules using functions, classes, file "
            "I/O, exceptions, regular expressions, tests, and reusable program "
            "structure."
        ),
        "featured": True,
        "display_order": 40,
    },
    {
        "title": "Systems Programming and Data Structures",
        "slug": "systems-programming-and-data-structures",
        "summary": (
            "A collection of low-level programming projects focused on memory, "
            "algorithms, data structures, and correctness."
        ),
        "category": ProjectCategory.INFRASTRUCTURE,
        "status": ProjectStatus.COMPLETED,
        "role": (
            "Implemented low-level programs focused on memory, algorithms, and "
            "data structures"
        ),
        "tech_stack": (
            "C, algorithms, memory management, pointers, data structures, "
            "debugging"
        ),
        "problem_context": (
            "Understanding lower-level programming improves debugging, "
            "performance awareness, and reasoning about how software behaves "
            "beneath high-level frameworks."
        ),
        "technical_approach": (
            "Implemented C programs involving arrays, algorithms, pointers, memory "
            "management, file handling, and data structures, with attention to "
            "correctness and style."
        ),
        "featured": True,
        "display_order": 50,
    },
]


class Command(BaseCommand):
    """Create or update the initial portfolio project records."""

    help = "Seed initial portfolio project records."

    def handle(self, *args: Any, **options: Any) -> None:
        created_count = 0
        updated_count = 0

        for record in PROJECT_RECORDS:
            slug = record["slug"]
            defaults = {key: value for key, value in record.items() if key != "slug"}

            _, created = Project.objects.update_or_create(
                slug=slug,
                defaults=defaults,
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded project records: {created_count} created, "
                f"{updated_count} updated."
            )
        )
