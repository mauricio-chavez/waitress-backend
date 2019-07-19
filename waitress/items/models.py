"""Items app models"""

from django.db import models

from waitress.food_sessions.models import FoodSession
from waitress.users.models import SessionUser


class Item(models.Model):
    """Base item model"""
    name = models.CharField('nombre', max_length=50)
    amount = models.FloatField('monto')

    class Meta:
        abstract = True
        verbose_name = 'artículo'


class PersonalItem(Item):
    """Model of an item with a owner"""
    owner = models.ForeignKey(
        verbose_name='propietario',
        to=SessionUser,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'artículo personal'
        verbose_name_plural = 'artículos personales'

    def __str__(self):
        """Returns a string representation of a item"""
        return f'{self.name} de {self.owner.user.email}'


class SharedItem(Item):
    """Model of a shared item"""
    food_session = models.ForeignKey(
        verbose_name='sesión de comida',
        to=FoodSession,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'artículo compartido'
        verbose_name_plural = 'artículos compartidos'

    def __str__(self):
        """Returns a string representation of a item"""
        return f'{self.name} en {self.food_session.name}'
