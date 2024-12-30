from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponseForbidden
from .utils import get_client_ip, is_suspicious_ip


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Honeypot Check
            if form.cleaned_data.get('honeypot'):
                return HttpResponseForbidden("Spam detected. Submission blocked.")
            
            # IP Validation
            user_ip = get_client_ip(request)
            if is_suspicious_ip(user_ip):
                return HttpResponseForbidden("Suspicious IP detected. Submission blocked.")

            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})


