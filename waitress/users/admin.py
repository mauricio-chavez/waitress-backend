"""Users admin site configuration"""

from django.contrib import admin

from .models import SessionUser


@admin.register(SessionUser)
class SessionUserAdmin(admin.ModelAdmin):
    """Admin View for SessionUser"""
    list_display = ('user', 'food_session', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user__email', 'food_session__name')
    ordering = ('food_session__name', 'user__email')
