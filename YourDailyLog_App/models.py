from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic that user is learning about"""
    topicName = models.CharField(max_length=200)
    dateAndTime = models.DateTimeField(auto_now_add=True)

    # When a user is deleted, all its topics will be deleted as well
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the string representation of the model"""
        return self.topicName
    # end function
# end class Topic

class Entry(models.Model):
    """Something specific about a topic (an Entry about a topic, that is)"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    entryText = models.TextField()
    dateAndTimeAdded = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Entries"
    # end class Meta

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.entryText) <= 50:
            return self.entryText

        return f"{self.entryText[: 50]}..."
    # end function
# end class Entry