# Generated by Django 5.0.2 on 2024-08-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_herosection_paragraph_alter_herosection_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Headling', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('info1', models.CharField(max_length=250)),
                ('info2', models.CharField(max_length=250)),
                ('info3', models.CharField(max_length=250)),
                ('info4', models.CharField(max_length=250)),
            ],
        ),
    ]