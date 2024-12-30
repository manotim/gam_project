from django.db import models

class Gallery(models.Model):
    PHOTO = 'photo'
    VIDEO = 'video'
    MEDIA_TYPE_CHOICES = [
        (PHOTO, 'Photo'),
        (VIDEO, 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default=PHOTO)
    media_file = models.FileField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.title} ({self.media_type.capitalize()})"

    def is_photo(self):
        return self.media_type == self.PHOTO

    def is_video(self):
        return self.media_type == self.VIDEO
