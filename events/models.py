from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    likes = models.ManyToManyField(User, related_name="event_likes", blank=True, null=True)

    def __str__(self):
        return self.event_name

    def total_likes(self):
        return self.likes.count()
