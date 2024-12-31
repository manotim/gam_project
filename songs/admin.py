from django.contrib import admin
from .models import Song, Album

class SongInline(admin.TabularInline):
    model = Song
    extra = 1

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    inlines = [SongInline]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'song_type', 'album', 'is_downloadable')
    list_filter = ('song_type', 'album')
