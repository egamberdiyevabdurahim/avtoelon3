from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from User.models import User


class Davlat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Viloyat(models.Model):
    name = models.CharField(max_length=50)
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE, related_name='viloyatlar')

    def __str__(self):
        return f'{self.davlat}/{self.name}'


class Shahar(models.Model):
    name = models.CharField(max_length=50)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE, related_name='shaharlar')

    def __str__(self):
        return f'{self.viloyat}/{self.name}'


class Model(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Rusum(models.Model):
    name = models.CharField(max_length=30)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='model_rusumi')

    def __str__(self):
        return f'{self.model}/{self.name}'


class Karobka(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Rang(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Yeyishi(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField(upload_to='Avto_photo/')


# class ViewedAvto(models.Model):
#     viewed_list = models.IntegerField(default=0)

# @reciever(post_save, sender=ViewedAvto)
# def create_viewedavto(sender, instance, created=False, **s):




class Avto(models.Model):
    XOLATSTATUS = [
        ('Avtosalon', 'Avtosalon'),
        ('Ishlagan', 'Ishlagan')
    ]

    SAVSTATUS = [
        ('Savdolashuv bor', 'Savdolashuv bor'),
        ('Yoq', 'Yoq')
    ]
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='avto_modeli', verbose_name='Modeli')
    rusum = models.ForeignKey(Rusum, on_delete=models.CASCADE, related_name='avto_rusumi', verbose_name='Rusumi')
    yili = models.IntegerField(verbose_name='Yili')
    savdolashuv = models.CharField(max_length=99, choices=SAVSTATUS, default='Yoq')
    photo = models.ManyToManyField(Photo, verbose_name='Rasm')
    xolati = models.CharField(max_length=99, choices=XOLATSTATUS, default='Ishlagan')
    yeyishi = models.ForeignKey(Yeyishi, on_delete=models.CASCADE, related_name='avto_yeyishi', verbose_name='Yeyishi')
    karobka = models.ForeignKey(Karobka, on_delete=models.CASCADE, related_name='avto_karobkasi', verbose_name='Karobka')
    rang = models.ForeignKey(Rang, on_delete=models.CASCADE, related_name='avto_rangi', verbose_name='Rangi')
    kraska_holati = models.CharField(max_length=50, verbose_name='Kraska Holati')
    shahar = models.ForeignKey(Shahar, on_delete=models.CASCADE, related_name='avto_shahari', verbose_name='Shahar')
    narhi = models.IntegerField(verbose_name='Narhi')
    dvigatel = models.CharField(max_length=3, verbose_name='Dvigatel Hajmi')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avto_user', verbose_name='User')
    data = models.DateField(auto_now_add=True)
    yana = models.TextField(verbose_name=f'qushimcha', null=True, blank=True)

    def __str__(self):
        return f'{self.rusum}/{self.narhi}/{self.shahar}'
