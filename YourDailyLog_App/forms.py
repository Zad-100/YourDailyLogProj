# This module lets us make forms for the users to enter and submit information

from django import forms

from .models import Topic # we will work with this user defined model

class TopicForm(forms.ModelForm):
    # Model Meta is basically used to change the behavior of your model fields
    # like changing order options,verbose_name and lot of other options. It’s
    # completely optional to add Meta class in your model.
    class Meta:
        model = Topic # this means that the form will be based on "Topic" model
        fields = ['topicName'] # only topicName field needed for this form/blank
        labels = {'topicName': ''} # telling Django to not create a label for 
                                   # the topicName field