from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry

from .forms import TopicForm, EntryForm # programmer defined

def index(request):
    """The homepage for Your Daily Log"""
    return render(request, "yourdailylog_app/index.html")
# end function index()

# A decorator is a directive before a function that alters the function how to
# behave; it applies to the function before it runs
# @ lets Python know that login_required() function is to be run before topics()
# login_required() checks whether a user is logged in, and Django runs the
# topics code only if they are.
# If the user isn't logged in they are redirected to the login page.

@login_required # restrict access to certain pages to logged-in users
def topics(request):
    """The topics page that shows all topics entered by a user"""
    topicNames = Topic.objects.order_by('dateAndTime')
    context = {'topicNames': topicNames} # context is to be passed to the
                                         # template so that it can work on it

    return render(request, "yourdailylog_app/topics.html", context)
# end function topics()

@login_required
def topic(request, topicID):
    """
       Show all the entries with their time stamp for a particular topic.
       The entries are shown in reverse chronological order.
    """
    topicName = Topic.objects.get(id=topicID)

    # the '-' sign before dateAndTimeAdded attribute is used to order in reverse
    # order, that is in descending order
    entries = topicName.entry_set.order_by("-dateAndTimeAdded")
    context = {'topicName': topicName, 'entries': entries}

    return render(request, 'yourdailylog_app/topic.html', context)
# end function topic()

@login_required
def new_topic(request):
    """
        Adds a new topic. Also redirects the user back to the topics page
        after the user has submitted the form with the new topic name
    """

    # 'POST' requests are made when the user requests to process a submitted
    # form
    # 'GET' requests are made when the request is to read information from the
    # server
    if request.method != 'POST': # that means the user requesting for a blank
                                 # form
                                 # 'GET' request (probably)
        # No data submitted; create a blank form
        formForNewTopic = TopicForm() # instance created of TopicForm
    else:
        # POST data submitted; process data
        formForNewTopic = TopicForm(data=request.POST)
        if formForNewTopic.is_valid():
            formForNewTopic.save()
            
            # redirect() takes in the name of a view and redirect the user to
            # that view
            return redirect('YourDailyLog_App:topics')

    # Display a blank or invalid form
    context = {"formForNewTopic": formForNewTopic}

    return render(request, 'yourdailylog_app/new_topic.html', context)
# end function new_topic()

@login_required
def new_entry(request, topicID):
    """
        Adds a new entry under a particular topic
    """
    topicName = Topic.objects.get(id=topicID)

    if request.method != 'POST':
        # No data submitted; create a blank form
        formForEntry = EntryForm() # new instance created
    else:
        # POST data submitted; process data
        formForEntry = EntryForm(data=request.POST)
        if formForEntry.is_valid():
            # commit is set to False - "don't save it to the database yet"
            newEntry = formForEntry.save(commit=False)
            newEntry.topic = topicName
            newEntry.save()

            return redirect('YourDailyLog_App:topic', topicID=topicID)

    # Display a blank or invalid form
    context = {"topicName": topicName, "formForEntry": formForEntry}
    return render(request, "yourdailylog_app/new_entry.html", context)
# end function new_entry()

@login_required
def edit_entry(request, entryID):
    """Edit an existing entry using its ID"""
    entry = Entry.objects.get(id=entryID)
    topicName = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with current entry
        formForEditing = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        # instance argument creates a form instance with current entry
        # data argument updates the form with the data from request.POST
        formForEditing = EntryForm(instance=entry, data=request.POST)
        
        if formForEditing.is_valid():
            formForEditing.save()

            return redirect("YourDailyLog_App:topic", topicID=topicName.id)

    context = {
        "entry": entry,
        "topicName": topicName,
        'formForEditing': formForEditing,
    }

    return render(request, 'yourdailylog_app/edit_entry.html', context)
# end function edit_entry()