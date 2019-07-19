"""Admin site settings"""

from django.contrib.auth import get_user_model
from django.contrib import admin


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    """Admin View for User"""
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
