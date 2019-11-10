#Import Dependencies
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length = 250)
    title_picture = models.CharField(max_length = 1000)

    def __str__(self):
        return self.title

class EventDetail(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_title = models.CharField(max_length = 250)
    event_picture = models.CharField(max_length = 1000)
    description = models.CharField(max_length = 5000)

    def __str__(self):
        return self.event_title