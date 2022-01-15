# This module lets us make forms for the users to enter and submit information

from django import forms
from django.db.models import fields

from .models import Topic # we will work with this user defined model
from .models import Entry # for users to make entries

class TopicForm(forms.ModelForm):
    """Form for adding a topic"""
    # Model Meta is basically used to change the behavior of your model fields
    # like changing order options,verbose_name and lot of other options. It’s
    # completely optional to add Meta class in your model.
    class Meta:
        model = Topic # this means that the form will be based on "Topic" model
        fields = ['topicName'] # only topicName field needed for this form/blank
        labels = {'topicName': ''} # telling Django to not create a label for 
                                   # the topicName field
    # end class Meta
# end class TopicForm

class EntryForm(forms.ModelForm):
    """Form for making entries"""
    class Meta:
        model = Entry
        fields = ['entryText']
        labels = {'entryName': ''}
        
        # Widgets: HTML form element; e.g.: single line text box, multi-line
        # text area, or a drop-down list
        # here the entry-text area becomes 100 columns wide
        widgets = {'entryText': forms.Textarea(attrs={'cols': 100})}
    # end class Meta
# end class EntryForm