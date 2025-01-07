from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, EventAttendee, EventSponsor
from django.utils import timezone
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.core.mail import send_mail
from django.conf import settings
from .forms import EventRegistrationForm

def event_list(request):
    query = request.GET.get('q')
    date = request.GET.get('date')
    location = request.GET.get('location')
    
    events = Event.objects.all().order_by('date')

    if query:
        events = events.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if date:
        parsed_date = parse_date(date)
        if parsed_date:
            events = events.filter(date__date=parsed_date)
    
    if location:
        events = events.filter(location__icontains=location)

    return render(request, 'events/event_list.html', {'events': events})


# Event Detail View
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    attendees = EventAttendee.objects.filter(event=event)
    sponsors = EventSponsor.objects.filter(event=event)
    return render(request, 'events/event_detail.html', {
        'event': event,
        'attendees': attendees,
        'sponsors': sponsors
    })

# Register Attendee View





def register_attendee(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.event = event
            attendee.save()
            # Send confirmation email
            send_mail(
                subject=f"Registration Confirmed for {event.name}",
                message=f"Hello {attendee.name},\n\nYou have successfully registered for {event.name} on {event.date} at {event.location}.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[attendee.email],
                fail_silently=False,
            )
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventRegistrationForm()
    return render(request, 'events/register_attendee.html', {'event': event, 'form': form})



