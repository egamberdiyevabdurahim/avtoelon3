# Generated by Django 5.0.1 on 2024-01-16 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0003_avto_slug_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avto',
            name='slug',
        ),
    ]
