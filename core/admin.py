# /home/kamusc/myproject/core/admin.py
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # Columns shown on the main list overview page
    list_display = ('title', 'created_at', 'is_published')

    # Clickable links to open the record editor page
    list_display_links = ('title',)

    # Instant sidebar filtering dropdown blocks
    list_filter = ('is_published', 'created_at')

    # Adds a search bar targeting specific fields
    search_fields = ('title', 'description')
