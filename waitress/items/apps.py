"""Items app"""

from django.apps import AppConfig
from django.db.models.signals import pre_save

from .signals import add_emoji_to_pizza


class ItemsConfig(AppConfig):
    """Items app config"""
    name = 'waitress.items'
    verbose_name = 'Artículos'

    def ready(self):
        """Connects the presave signal with item model"""
        pre_save.connect(add_emoji_to_pizza, sender='items.PersonalItem')
        pre_save.connect(add_emoji_to_pizza, sender='items.SharedItem')
