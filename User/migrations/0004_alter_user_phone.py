# Generated by Django 5.0.1 on 2024-01-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
