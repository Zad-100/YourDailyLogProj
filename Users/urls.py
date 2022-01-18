"""Defines URL patterns for users"""

from django.urls import path, include

from . import views # to write programmer defined views function

app_name = 'Users'
urlpatterns = [
    # Include default authentication urls
    path("", include("django.contrib.auth.urls")),

    # Registration page
    path("register/", views.register, name="register"),
]