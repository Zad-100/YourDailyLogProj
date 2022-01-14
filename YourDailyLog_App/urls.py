"""Defines URL patterns for YourDailyLog_App"""

from django.urls import path

from . import views

app_name = "YourDailyLog_App"
urlpatterns = [
    # Homepage
    # The URL route is left blank as it defaults to the base django page
    # The requested URL is routed to its respective view 
    # The second argument specifies which views file to call in views.py
    # The third argument assigns a name to this URL pattern so that we can refer
    # to it in other programs
    path("", views.index, name='index'),

    # Topics page - shows all the topics for a user
    path('topics/', views.topics, name="topics"),

    # Individual topic page which shows the entries made by user
    # Uses the topic's ID assigned automatically to route to that page
    path("topics/<int:topicID>/", views.topic, name='topic'),

    # Page for adding a new topic
    path("new_topic/", views.new_topic, name="new_topic"),

    # Page for making a new entry under a topic using its topic id
    path("new_entry/<int:topicID>/", views.new_entry, name="new_entry"),
]