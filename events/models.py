from django.db import models
from choir.models import Singer  # Ensure the Singer model is imported
from gallery.models import Gallery

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    featured_singers = models.ManyToManyField(Singer, related_name='events')
    poster = models.ImageField(upload_to='events/posters/', blank=True, null=True)
    gallery_items = models.ManyToManyField(Gallery, blank=True, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

class EventAttendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

class EventSponsor(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsors/logos/')
