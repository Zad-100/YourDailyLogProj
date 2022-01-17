"""Defines URL patterns for users"""

from django.urls import path, include

app_name = 'Users'
urlpatterns = [
    # Include default authentication urls
    path("", include("django.contrib.auth.urls")),
]