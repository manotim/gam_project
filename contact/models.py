from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)  # Name of the sender
    email = models.EmailField()  # Sender's email address
    subject = models.CharField(max_length=255)  # Subject of the message
    message = models.TextField()  # Detailed message
    date_sent = models.DateTimeField(auto_now_add=True)  # Auto timestamp
    is_resolved = models.BooleanField(default=False)  # Tracks if the message has been addressed

    class Meta:
        ordering = ['-date_sent']

    def __str__(self):
        return f"{self.subject} - {self.name}"
