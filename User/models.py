from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS = [
        ('Admin', 'Admin'),
        ('Adminstrator', 'Adminstrator'),
        ('User', 'User'),
    ]

    status = models.CharField(max_length=30, choices=STATUS, default='User')
    phone = models.CharField(max_length=14, null=True, blank=True)
    photo = models.ImageField(upload_to='user_photos/')

    def __str__(self):
        return self.username
