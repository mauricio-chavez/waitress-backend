"""Items app models"""

from django.db import models
from django.contrib.auth import get_user_model

from waitress.food_sessions.models import FoodSession
from waitress.users.models import SessionUser


class Item(models.Model):
    """Core item model"""
    name = models.CharField('nombre', max_length=50)
    amount = models.FloatField('monto')

    class Meta:
        verbose_name = 'artículo'


class PersonalItem(models.Model):
    """Model of an item with a owner"""
    item = models.OneToOneField('Item', on_delete=models.CASCADE)
    owner = models.ForeignKey(SessionUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'artículo personal'
        verbose_name_plural = 'artículos personales'


class SharedItem(models.Model):
    """Model of a shared item"""
    item = models.OneToOneField('Item', on_delete=models.CASCADE)
    food_session = models.ForeignKey(FoodSession, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'artículo compartido'
        verbose_name_plural = 'artículos compartidos'
