from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    home_place = models.CharField(max_length=100)
    home_church = models.CharField(max_length=100)
    current_place = models.CharField(max_length=100)
    current_church = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, blank=True, null=True)
    voice = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='singers_photos/')
