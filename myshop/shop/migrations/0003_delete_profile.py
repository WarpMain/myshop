# Generated by Django 4.1.13 on 2024-06-06 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]