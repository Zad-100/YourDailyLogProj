from django.db import models

class Topic(models.Model):
    """A topic that user is learning about"""
    topicName = models.CharField(max_length=200)
    dateAndTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the string representation of the model"""
        return self.topicName

class Entry(models.Model):
    """Something specific about a topic (an Entry about a topic, that is"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    entryText = models.TextField()
    dateAndTimeAdded = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.entryText[: 50]}..."