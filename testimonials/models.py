from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)  # Name of the person giving the testimonial
    email = models.EmailField(blank=True, null=True)  # Optional contact email
    message = models.TextField()  # Testimonial message
    photo = models.ImageField(upload_to='testimonials/photos/', blank=True, null=True)  # Optional photo
    rating = models.PositiveSmallIntegerField(
        default=5,
        help_text="Rating from 1 to 5"
    )  # Rating out of 5
    date_submitted = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    is_approved = models.BooleanField(default=False)  # Admin approval before display

    class Meta:
        ordering = ['-date_submitted']

    def __str__(self):
        return f"{self.name} - {self.rating}/5"
