# Generated by Django 5.0.2 on 2024-08-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_contactformlog_action_time_contactformlog_is_error_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformlog',
            name='error_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
