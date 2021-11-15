"""Defines URL patterns for YourDailyLog_App"""

from django.urls import path

from . import views

app_name = "YourDailyLog_App"
urlpatterns = [
    # Homepage
    path("", views.index, name='index'),
]