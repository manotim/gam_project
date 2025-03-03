# gallery/views.py
from django.shortcuts import render, get_object_or_404
from .models import Gallery

def gallery_list(request):
    """View to list all gallery items."""
    photos = Gallery.objects.filter(media_type=Gallery.PHOTO)
    videos = Gallery.objects.filter(media_type=Gallery.VIDEO)
    return render(request, 'gallery/gallery_list.html', {'photos': photos, 'videos': videos})

def gallery_detail(request, pk):
    """View to display details of a specific gallery item."""
    item = get_object_or_404(Gallery, pk=pk)
    return render(request, 'gallery/gallery_detail.html', {'item': item})
