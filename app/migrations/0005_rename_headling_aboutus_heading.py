# Generated by Django 5.0.2 on 2024-08-12 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_counter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='Headling',
            new_name='Heading',
        ),
    ]
