from django.contrib import admin
from .models import Event, EventAttendee, EventSponsor

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location', 'created_at']
    list_filter = ['date', 'location']
    search_fields = ['name', 'description']

@admin.register(EventAttendee)
class EventAttendeeAdmin(admin.ModelAdmin):
    list_display = ['event', 'name', 'email']
    search_fields = ['name', 'email']

@admin.register(EventSponsor)
class EventSponsorAdmin(admin.ModelAdmin):
    list_display = ['event', 'name']
    search_fields = ['name']
