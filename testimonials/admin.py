from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'date_submitted', 'is_approved')
    search_fields = ('name', 'email', 'message')
    list_filter = ('rating', 'is_approved', 'date_submitted')
    ordering = ('-date_submitted',)
    actions = ['approve_testimonials']

    @admin.action(description='Approve selected testimonials')
    def approve_testimonials(self, request, queryset):
        queryset.update(is_approved=True)
