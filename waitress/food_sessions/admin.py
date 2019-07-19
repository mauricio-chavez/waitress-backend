"""Admin site configuration for food sessions app"""

from django.contrib import admin

from .models import FoodSession


@admin.register(FoodSession)
class FoodSessionAdmin(admin.ModelAdmin):
    """Admin View for FoodSession"""

    list_display = ('name', 'admin', 'is_active')
    list_filter = ('created', 'last_modified')
    search_fields = ('name', 'created', 'last_modified')
    ordering = ('is_active', 'last_modified', 'created', 'name')
