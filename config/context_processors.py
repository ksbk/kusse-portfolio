from typing import Any
from django.http import HttpRequest

def site_metadata(request: HttpRequest) -> dict[str, Any]:
    return {
        "site": {
            "name": "Kusse Sukuta Bersha",
            "description": "Professional profile and portfolio of Kusse Sukuta Bersha.",
        }
    }
