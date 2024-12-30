from django.contrib import admin
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'uploaded_by', 'uploaded_at')
    search_fields = ('title', 'uploaded_by')
    list_filter = ('media_type', 'uploaded_at')
    ordering = ('-uploaded_at',)
