"""Items signals"""

def add_emoji_to_pizza(sender, instance, **kwargs):
    """Adds a pizza emoji if pizza is in item name"""
    if 'pizza' in instance.name.lower():
        instance.name += ' 🍕'

# def remove_