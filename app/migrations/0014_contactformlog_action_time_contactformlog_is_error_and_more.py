# Generated by Django 5.0.2 on 2024-08-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_contactformlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformlog',
            name='action_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contactformlog',
            name='is_error',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contactformlog',
            name='is_success',
            field=models.BooleanField(default=False),
        ),
    ]
