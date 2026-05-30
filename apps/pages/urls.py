"""URL routes for placeholder page scaffolding."""

from django.urls import path

from . import views


app_name = "pages"

urlpatterns = [
    path("", views.placeholder, name="placeholder"),
]
