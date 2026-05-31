"""URL routes for structured project portfolio pages."""

from django.urls import path

from .views import ProjectIndexView

app_name = "projects"

urlpatterns = [
    path("", ProjectIndexView.as_view(), name="index"),
]