"""Food sessions models"""

from django.contrib.auth import get_user_model
from django.db import models


class FoodSession(models.Model):
    """Food Session model"""
    name = models.CharField('Nombre', max_length=50)
    is_active = models.BooleanField('activa', default=False)
    admin = models.ForeignKey(
        verbose_name='administrador',
        to=get_user_model(),
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField('fecha de creacion', auto_now=True)
    last_modified = models.DateTimeField(
        verbose_name='última modificación',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'sesión de comida'
        verbose_name_plural = 'sesiones de comida'
