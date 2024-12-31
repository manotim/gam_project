from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, HttpResponseForbidden
from .models import Song, Album, Lyrics

# Song List View
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})

# Song Detail View
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    lyrics = Lyrics.objects.filter(song=song).first()
    return render(request, 'songs/song_detail.html', {'song': song, 'lyrics': lyrics})

# Song Download View
def song_download(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if song.is_downloadable:
        if song.song_type == Song.AUDIO and song.audio_file:
            return FileResponse(song.audio_file.open(), as_attachment=True)
        if song.song_type == Song.VIDEO and song.video_file:
            return FileResponse(song.video_file.open(), as_attachment=True)
    return HttpResponseForbidden("Downloading is not allowed for this song.")

# Album List View
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'songs/album_list.html', {'albums': albums})

# Album Detail View
def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = Song.objects.filter(album=album)
    return render(request, 'songs/album_detail.html', {'album': album, 'songs': songs})



def assign_song_to_album(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    albums = Album.objects.all()
    
    if request.method == 'POST':
        album_id = request.POST.get('album_id')
        album = get_object_or_404(Album, id=album_id)
        song.album = album
        song.save()
        return redirect('song_list')

    return render(request, 'songs/assign_song.html', {'song': song, 'albums': albums})
