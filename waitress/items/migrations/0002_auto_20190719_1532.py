# Generated by Django 2.2.3 on 2019-07-19 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalitem',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.SessionUser', verbose_name='propietario'),
        ),
        migrations.AlterField(
            model_name='shareditem',
            name='food_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_sessions.FoodSession', verbose_name='sesión de comida'),
        ),
    ]