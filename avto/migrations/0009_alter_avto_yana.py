# Generated by Django 5.0.1 on 2024-02-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0008_remove_viloyat_davlat_remove_shahar_viloyat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avto',
            name='yana',
            field=models.TextField(blank=True, null=True, verbose_name="qo'shimcha"),
        ),
    ]