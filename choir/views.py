from django.shortcuts import render
from .models import Singer

def singers_list(request):
    singers = Singer.objects.all()  # Fetch all singers
    return render(request, 'choir/singers_list.html', {'singers': singers})
