"""URL routes for structured project portfolio pages."""

from django.urls import path

from .views import ProjectDetailView, ProjectIndexView

app_name = "projects"

urlpatterns = [
    path("", ProjectIndexView.as_view(), name="index"),
    path("<slug:slug>/", ProjectDetailView.as_view(), name="detail"),
]