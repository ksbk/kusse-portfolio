from typing import Any

from django.conf import settings
from django.http import HttpRequest


def site_metadata(request: HttpRequest) -> dict[str, Any]:
    return {
        "site": {
            "name": getattr(settings, "SITE_NAME", "Kusse Sukuta Bersha"),
            "description": getattr(
                settings,
                "SITE_DESCRIPTION",
                "Professional profile and portfolio of Kusse Sukuta Bersha.",
            ),
            "social_links": {
                "github": getattr(settings, "SITE_GITHUB_URL", ""),
                "linkedin": getattr(settings, "SITE_LINKEDIN_URL", ""),
            },
        },
    }
