from django.shortcuts import render
from .models import Singer
from gallery.models import Gallery



def singers_list(request):
    singers = Singer.objects.all()  # Fetch all singers
    recent_photos = Gallery.objects.filter(media_type=Gallery.PHOTO)[:5]
    recent_videos = Gallery.objects.filter(media_type=Gallery.VIDEO)[:5]
    return render(request, 'choir/singers_list.html', {'singers': singers, 'recent_photos': recent_photos, 'recent_videos': recent_videos})
