from django.db import models

class Topic(models.Model):
    """A topic that user is learning about"""
    topicName = models.CharField(max_length=200)
    dateAndTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the string representation of the model"""
        return self.topicName