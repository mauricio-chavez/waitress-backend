"""Admin site config for items"""

from django.contrib import admin

from .models import PersonalItem, SharedItem


@admin.register(PersonalItem)
class PersonalItemAdmin(admin.ModelAdmin):
    """Admin View for PersonalItem"""
    list_display = ('name', 'amount', 'owner')
    list_filter = ('amount', 'owner__is_active')
    search_fields = ('name', 'amount', 'owner__user__email')
    ordering = ('name', 'amount', 'owner__user__email')


@admin.register(SharedItem)
class SharedItemdmin(admin.ModelAdmin):
    """Admin View for SharedItem"""
    list_display = ('name', 'amount', 'food_session')
    list_filter = ('amount', 'food_session__is_active')
    search_fields = ('name', 'amount', 'food_session__name')
    ordering = ('name', 'amount', 'food_session__name')
