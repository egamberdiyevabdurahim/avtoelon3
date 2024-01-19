from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

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


class Photo(models.Model):
    photo = models.ImageField(upload_to='Avto_photo/')


# class ViewedAvto(models.Model):
#     viewed_list = models.IntegerField(default=0)

# @reciever(post_save, sender=ViewedAvto)
# def create_viewedavto(sender, instance, created=False, **s):




class Avto(models.Model):
    XOLATSTATUS = [
        ('Avtosalon', 'Avtosalon'),
        ('Ishlagan', 'Ishlagan'),
    ]

    SAVSTATUS = [
        ('Savdolashuv bor', 'Savdolashuv bor'),
        ('Yoq', 'Yoq'),
    ]

    Yili = (
        ('2000', '2000'), ('2001', '2001'), ('2002', '2002'),
        ('2003', '2003'), ('2004', '2004'), ('2005', '2005'),
        ('2006', '2006'), ('2007', '2007'), ('2008', '2008'),
        ('2009', '2009'), ('2010', '2010'), ('2011', '2011'),
        ('2012', '2012'), ('2013', '2013'), ('2014', '2014'),
        ('2015', '2015'), ('2016', '2016'), ('2017', '2017'),
        ('2018', '2018'), ('2019', '2019'), ('2020', '2020'),
        ('2021', '2021'), ('2022', '2022'), ('2023', '2023'),
        ('2024', '2024'),
        )

    Yoqilgi_turi = (
        ('Benzin', 'Benzin'), ('Gaz', 'Gaz'),
        ('Elektr', 'Elektr'), ('Benzin/Gaz', 'Benzin/Gaz'),
        ('Dizel', 'Dizel'), ('Gibrid', 'Gibrid'),
        )

    Uzatish_qutisi = (
        ('Mexanika', 'Mexanika'), ('Avtomat', 'Avtomat'),
        ('Tiptronik', 'Tiptronik'), ('Variator', 'Variator'),
        ('Robot', 'Robot'),
        )

    Kuzov = (
        ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'),
        ('Yo\'ltanlamas', 'Yo\'ltanlamas'), ('Universal', 'Universal'),
        ('Karbiolet', 'Karbiolet'), ('Krossover', 'Krossover'),
        ('Kupe', 'Kupe'), ('Limuzin', 'Limuzin'),
        ('Mikroavtobus', 'Mikroavtobus'), ('Miniven', 'Miniven'),
        ('Mikroven', 'Mikroven'), ('Pikup', 'Pikup'),
        ('Rodster', 'Rodster'), ('Furgon', 'Furgon'),
        )

    Rang = (
        ('Oq', 'Oq'), ('Qaymoq rang', 'Qaymoq rang'),
        ('Delfin', 'Delfin'), ('Mokriy asfalt', 'Mokriy asfalt'),
        ('Qora', 'Qora'), ('Kumush rang', 'Kumush rang'),
        ('Saxara (qum rang)', 'Saxara (qum rang)'), ('Sadaf-jigarrang', 'Sadaf-jigarrang'),
        ('Sariq-yashil rang', 'Sariq-yashil rang'), ('Ko\'k xavorang', 'Ko\'k xavorang'),
        ('Olcha', 'Olcha'), ('K\'k', 'K\'k'),
        ('Qizil', 'Qizil'), ('Kulrang', 'Kulrang'),
        ('Jigarrang', 'Jigarrang'), ('Bronza', 'Bronza'),
        ('Xameleon', 'Xameleon'), ('Feruza', 'Feruza'),
        ('To\'q-qizil', 'To\'q-qizil'), ('Moviy', 'Moviy'),
        ('Sariq', 'Sariq'), ('Yashil', 'Yashil'),
        ('Och-binafsha-rang', 'Och-binafsha-rang'), ('Oltin rang', 'Oltin rang'),
        ('To\'q-sariq', 'To\'q-sariq'), ('Pushti rang', 'Pushti rang'),
        ('Binafsha rang', 'Binafsha rang'), ('To\'q-ko\'k', 'To\'q-ko\'k'),
        )

    Kraska_Holati = (
        ('Kraska toza', 'Kraska toza'), ('Kraskasi bor', 'Kraskasi bor'),
        ('Pyatno bor', 'Pyatno bor'), ('To\'liq kraskalangan', 'To\'liq kraskalangan'),
        )

    Uzatma = (
        ('Oldi', 'Oldi'), ('Orqa', 'Orqa'), ('To\'liq', 'To\'liq'),
        )

    Valyuta = (
        ('UZS', 'UZS'), ('USD', 'USD'),
        ('EUR', 'EUR'), ('RUB', 'RUB'),
        ('SAR', 'SAR'), ('CNY', 'CNY'),
        )

    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='avto_modeli', verbose_name='Modeli')
    rusum = models.ForeignKey(Rusum, on_delete=models.CASCADE, related_name='avto_rusumi', verbose_name='Rusumi')
    yili = models.CharField(max_length=5, choices=Yili, verbose_name='Yili')
    savdolashuv = models.CharField(max_length=99, choices=SAVSTATUS, default='Yoq')
    yurgani = models.IntegerField(null=True)
    uzatma = models.CharField(max_length=10, choices=Uzatma, default='Oldi')
    photo = models.ManyToManyField(Photo, verbose_name='Rasm')
    xolati = models.CharField(max_length=99, choices=XOLATSTATUS, default='Ishlagan')
    yeyishi = models.CharField(max_length=50, choices=Yoqilgi_turi, verbose_name='Yeyishi')
    karobka = models.CharField(max_length=50, choices=Uzatish_qutisi, verbose_name='Karobka')
    rang = models.CharField(max_length=50, choices=Rang, verbose_name='Rangi')
    kraska_holati = models.CharField(max_length=50, choices=Kraska_Holati, verbose_name='Kraska Holati')
    shahar = models.ForeignKey(Shahar, on_delete=models.CASCADE, related_name='avto_shahari', verbose_name='Shahar')
    narhi = models.IntegerField(verbose_name='Narhi')
    valyuta = models.CharField(max_length=5, choices=Valyuta, default='UZS')
    dvigatel = models.CharField(max_length=3, verbose_name='Dvigatel Hajmi')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avto_user', verbose_name='User')
    data = models.DateField(auto_now_add=True)
    viewed_list = models.IntegerField(default=0)
    yana = models.TextField(verbose_name=f'qushimcha', null=True, blank=True)

    # @property
    # def sum_of_likes(self):
    #     return self.likes.user.count()
    def sum_of_vieved_list(self, *args, **kwargs):
        self.viewed_list = self.viewed_list+1
        super(Avto, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.rusum}/{self.narhi}/{self.shahar}'


class Like(models.Model):
    avto = models.OneToOneField(Avto, on_delete=models.CASCADE, related_name='likes')
    user = models.ManyToManyField(User)
