"""Bills models"""

from django.db import models

from waitress.food_sessions.models import FoodSession
from waitress.users.models import SessionUser


class FoodSessionBill(models.Model):
    """Session bill model"""
    food_session = models.OneToOneField(FoodSession, on_delete=models.CASCADE)
    total_amount = models.FloatField('monto total')

    class Meta:
        verbose_name = 'cuenta de la sesión de comida'
        verbose_name_plural = 'cuentas de sesiones de comida'

    def __str__(self):
        """Returns a string representation of the bill"""
        return f'{self.food_session.name} - ${self.total_amount}'


class SharedBill(models.Model):
    """Shared bill model"""
    food_session = models.OneToOneField(FoodSession, on_delete=models.CASCADE)
    total_per_person = models.FloatField('total por persona')
    total_amount = models.FloatField('monto total')

    class Meta:
        verbose_name = 'cuenta compartida'
        verbose_name_plural = 'cuentas compartidas'

    def __str__(self):
        """Returns a string representation of the bill"""
        return f'{self.food_session.name} - ${self.total_amount}'


class PersonalBill(models.Model):
    """Bill attached to a user"""
    user = models.ForeignKey(SessionUser, on_delete=models.CASCADE)
    total_amount = models.FloatField('monto total')

    class Meta:
        verbose_name = 'cuenta personal'
        verbose_name_plural = 'cuentas personales'

    def __str__(self):
        """Returns a string representation of the bill"""
        return f'{self.user.user.email} - ${self.total_amount}'
