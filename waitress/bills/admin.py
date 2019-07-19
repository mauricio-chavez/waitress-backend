"""Admin site for bills apps"""

from django.contrib import admin

from .models import FoodSessionBill, SharedBill, PersonalBill


@admin.register(FoodSessionBill)
class FoodSessionBillAdmin(admin.ModelAdmin):
    """Admin View for FoodSessionBill"""
    list_display = ('food_session', 'total_amount')
    list_filter = ('food_session__is_active', 'total_amount')
    search_fields = (
        'food_session__name', 'food_session__admin__email', 'total_amount'
    )
    ordering = ('food_session__name', 'total_amount')


@admin.register(SharedBill)
class SharedBillAdmin(admin.ModelAdmin):
    """Admin View for SharedBill"""
    list_display = ('food_session', 'total_per_person', 'total_amount')
    list_filter = (
        'food_session__is_active',
        'total_per_person', 'total_amount'
    )
    search_fields = (
        'food_session__name', 'food_session__admin__email',
        'total_per_person', 'total_amount'
    )
    ordering = ('food_session__name', 'total_per_person', 'total_amount')


@admin.register(PersonalBill)
class PersonalBillAdmin(admin.ModelAdmin):
    """Admin View for PersonalBill"""
    list_display = ('user', 'total_amount')
    list_filter = ('user__is_active', 'total_amount')
    search_fields = (
        'user__user__email', 'user__is_active', 'total_amount'
    )
    ordering = ('user__user__email', 'total_amount')
