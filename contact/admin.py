from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent', 'is_resolved')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('is_resolved', 'date_sent')
    ordering = ('-date_sent',)
    actions = ['mark_as_resolved']

    @admin.action(description='Mark selected messages as resolved')
    def mark_as_resolved(self, request, queryset):
        queryset.update(is_resolved=True)
