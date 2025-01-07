from django import forms
from .models import EventAttendee

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventAttendee
        fields = ['name', 'email']
