"""Defines URL patterns for YourDailyLog_App"""

from django.urls import path

from . import views

app_name = "YourDailyLog_App"
urlpatterns = [
    # Homepage
    path("", views.index, name='index'),

    # Topics page - shows all the topics for a user
    path('topics/', views.topics, name="topics"),

    # Individual topic page which shows the entries made by user
    path("topics/<int:topicID>/", views.topic, name='topic'),
]