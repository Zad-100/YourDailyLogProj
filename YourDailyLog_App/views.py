from django.shortcuts import render

from .models import Topic

def index(request):
    """The homepage for Your Daily Log"""
    return render(request, "yourdailylog_app/index.html")

def topics(request):
    """The topics page that shows all topics entered by a user"""
    topicNames = Topic.objects.order_by('dateAndTime')
    context = {'topicNames': topicNames}

    return render(request, "yourdailylog_app/topics.html", context)

def topic(request, topicID):
    """
       Show all the entries with their time stamp for a particular topic.
       The entries are shown in reverse chronological order.
    """
    topicName = Topic.objects.get(id=topicID)
    entries = topicName.entry_set.order_by("-dateAndTimeAdded")
    context = {'topicName': topicName, 'entries': entries}

    return render(request, 'yourdailylog_app/topic.html', context)
