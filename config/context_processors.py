from typing import Any

from django.conf import settings
from django.http import HttpRequest

from apps.pages.navigation import get_navigation


def _sanitize_public_link(url: str) -> str:
    normalized = url.strip()
    lowered = normalized.lower()

    if not normalized:
        return ""

    blocked_tokens = ("your-username", "example.com", "placeholder", "lorem")
    if any(token in lowered for token in blocked_tokens):
        return ""

    return normalized


def site_metadata(request: HttpRequest) -> dict[str, Any]:
    context: dict[str, Any] = {
        "site": {
            "name": getattr(settings, "SITE_NAME", "Kusse Sukuta Bersha"),
            "description": getattr(
                settings,
                "SITE_DESCRIPTION",
                "Professional profile and portfolio of Kusse Sukuta Bersha.",
            ),
            "social_links": {
                "github": _sanitize_public_link(getattr(settings, "SITE_GITHUB_URL", "")),
                "linkedin": _sanitize_public_link(getattr(settings, "SITE_LINKEDIN_URL", "")),
            },
        },
    }

    context.update(get_navigation(request))
    return context
