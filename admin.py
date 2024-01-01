from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'mood')  # Customize the display columns in the admin list view
    search_fields = ['date_created']  # Add search functionality for date_created field

admin.site.register(Entry, EntryAdmin)
