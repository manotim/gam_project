from django.contrib import admin
from .models import Singer

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'home_place', 'current_place', 'profession')
    search_fields = ('name', 'home_place', 'current_place', 'profession')
    list_filter = ('position', 'home_church', 'current_church')
    ordering = ('name',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('name','voice', 'position', 'profession', 'photo')
        }),
        ('Location', {
            'fields': ('home_place', 'home_church', 'current_place', 'current_church')
        }),
    )
