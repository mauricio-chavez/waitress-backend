"""Admin site config for items"""

from django.contrib import admin

from .models import Item, PersonalItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Admin View for Item"""
    list_display = ('name', 'amount')
    list_filter = ('amount',)
    search_fields = ('name', 'amount')
    ordering = ('name', 'amount')


@admin.register(PersonalItem)
class PersonalItemAdmin(admin.ModelAdmin):
    """Admin View for PersonalItem"""
    list_display = ('item', 'owner')
    list_filter = ('item', 'owner')
    search_fields = ('item', 'owner')
    ordering = ('item', 'owner')