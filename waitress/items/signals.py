"""Items signals"""


def add_emojis(sender, instance, **kwargs):
    """Adds emojis if something special is in item name"""
    if 'pizza' in instance.name.lower() and not instance.name.endswith('🍕'):
        instance.name += ' 🍕'
    if 'taco' in instance.name.lower() and not instance.name.endswith('🌮'):
        instance.name += ' 🌮'
