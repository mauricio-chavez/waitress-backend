"""Bills models"""

from django.db import models

from waitress.food_sessions.models import FoodSession
from waitress.users.models import SessionUser


class FoodSessionBill:
    """Session bill model"""
    food_session = models.OneToOneField(FoodSession, on_delete=models.CASCADE)
    total_amount = models.FloatField('monto total')


class PersonalBill:
    """Bill attached to a user"""
    user = models.ForeignKey(SessionUser, on_delete=models.CASCADE)
    food_session_bill = models.ForeignKey(
        to='FoodSessionBill',
        on_delete=models.CASCADE
    )
    total_amount = models.FloatField('monto total')