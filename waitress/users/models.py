"""Users models"""

from django.contrib.auth import get_user_model
from django.db import models

from waitress.food_sessions.models import FoodSession


class SessionUser(models.Model):
    """User with a session"""
    user = models.ForeignKey(
        verbose_name='usuario',
        to=get_user_model(),
        on_delete=models.CASCADE,
    )
    food_session = models.ForeignKey(
        verbose_name='sesión de comida',
        to=FoodSession,
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        verbose_name='activo',
        default=False
    )

    class Meta:
        verbose_name = 'usuario de sesión'
        verbose_name_plural = 'usuarios de sesión'

    def __str__(self):
        """Returns a string representation of a session user"""
        return f'{self.user.email} en {self.food_session.name}'
