from dataclasses import dataclass
from typing import Any

from django.http import HttpRequest
from django.urls import NoReverseMatch, reverse


@dataclass(frozen=True)
class NavigationItem:
    label: str
    url_name: str
    match_view_name: str = ""
    match_app_name: str = ""


MAIN_NAV = (
    NavigationItem("Home", "pages:home", match_view_name="pages:home"),
    NavigationItem("About", "pages:about", match_view_name="pages:about"),
    NavigationItem("Research", "pages:research", match_view_name="pages:research"),
    NavigationItem("Projects", "projects:index", match_app_name="projects"),
    NavigationItem("CV", "pages:cv", match_view_name="pages:cv"),
    NavigationItem("Contact", "pages:contact", match_view_name="pages:contact"),
)

FOOTER_NAV = {
    "explore": (
        NavigationItem("About", "pages:about", match_view_name="pages:about"),
        NavigationItem("Projects", "projects:index", match_app_name="projects"),
        NavigationItem("Research", "pages:research", match_view_name="pages:research"),
        NavigationItem("CV", "pages:cv", match_view_name="pages:cv"),
    ),
    "connect": (
        NavigationItem("Contact", "pages:contact", match_view_name="pages:contact"),
    ),
}

FOOTER_CONTENT = {
    "brand_mark_fallback": "KP",
    "role": "Engineer. Researcher. Problem solver.",
    "tagline": "Practical software, research tools, and clear technical delivery.",
    "updates_heading": "Stay updated",
    "updates_text": "Follow new projects, research notes, and writing.",
    "availability_text": "Open to new opportunities.",
}


def get_navigation(request: HttpRequest) -> dict[str, Any]:
    return {
        "home_url": _resolve_url("pages:home", fallback="/"),
        "contact_url": _resolve_url("pages:contact", fallback="/contact/"),
        "main_nav": _resolve_items(MAIN_NAV, request),
        "footer_nav": {
            group: _resolve_items(items, request)
            for group, items in FOOTER_NAV.items()
        },
        "footer": FOOTER_CONTENT,
    }


def _resolve_items(items: tuple[NavigationItem, ...], request: HttpRequest) -> list[dict[str, Any]]:
    resolved_items: list[dict[str, Any]] = []

    for item in items:
        try:
            url = reverse(item.url_name)
        except NoReverseMatch:
            continue

        resolved_items.append(
            {
                "label": item.label,
                "url": url,
                "is_active": _is_active(item, request),
            }
        )

    return resolved_items


def _resolve_url(url_name: str, fallback: str = "") -> str:
    try:
        return reverse(url_name)
    except NoReverseMatch:
        return fallback


def _is_active(item: NavigationItem, request: HttpRequest) -> bool:
    resolver_match = request.resolver_match

    if resolver_match is None:
        return False

    if item.match_app_name and resolver_match.app_name == item.match_app_name:
        return True

    return bool(item.match_view_name and resolver_match.view_name == item.match_view_name)
