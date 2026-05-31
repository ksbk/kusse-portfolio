"""URL routes for placeholder page scaffolding."""

from django.urls import path

from . import views


app_name = "pages"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("research/", views.ResearchView.as_view(), name="research"),
    path("cv/", views.CVView.as_view(), name="cv"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
