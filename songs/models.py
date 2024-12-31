from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums/covers/')

class Song(models.Model):
    AUDIO = 'audio'
    VIDEO = 'video'
    SONG_TYPE_CHOICES = [
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    ]

    title = models.CharField(max_length=255)
    song_type = models.CharField(max_length=10, choices=SONG_TYPE_CHOICES, default=AUDIO)
    description = models.TextField(blank=True, null=True)
    audio_file = models.FileField(upload_to='songs/audio/', blank=True, null=True)
    video_file = models.FileField(upload_to='songs/video/', blank=True, null=True)
    is_downloadable = models.BooleanField(default=False)
    uploaded_by = models.CharField(max_length=255, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_download_url(self):
        """Returns the download URL if the song is downloadable."""
        if self.is_downloadable:
            if self.song_type == self.AUDIO and self.audio_file:
                return self.audio_file.url
            if self.song_type == self.VIDEO and self.video_file:
                return self.video_file.url
        return None



class Lyrics(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE)
    content = models.TextField()
