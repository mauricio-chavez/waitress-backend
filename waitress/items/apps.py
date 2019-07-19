"""Items app"""

from django.apps import AppConfig
from django.db.models.signals import pre_save

from .signals import add_emojis


class ItemsConfig(AppConfig):
    """Items app config"""
    name = 'waitress.items'
    verbose_name = 'Artículos'

    def ready(self):
        """Connects the presave signal with item model"""
        pre_save.connect(add_emojis, sender='items.PersonalItem')
        pre_save.connect(add_emojis, sender='items.SharedItem')
