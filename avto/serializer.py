from rest_framework import serializers

from avto.models import (Davlat, Viloyat, Shahar, Model, Rusum,
                        Photo, Avto)


# class ViewedAvtoSer(serializers.ModelSerializer):
#     class Meta:
#         model = ViewedAvto
#         fields = ['id', 'viewed_list']


class DavlatSer(serializers.ModelSerializer):
    class Meta:
        model = Davlat
        fields = '__all__'


class ViloyatSer(serializers.ModelSerializer):
    class Meta:
        model = Viloyat
        fields = '__all__'


class ShaharSer(serializers.ModelSerializer):
    class Meta:
        model = Shahar
        fields = '__all__'


class ModelSer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class RusumSer(serializers.ModelSerializer):
    class Meta:
        model = Rusum
        fields = '__all__'


class PhotoSer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class AvtoSer(serializers.ModelSerializer):
    class Meta:
        model = Avto
        fields = '__all__'
        read_only_fields = ['photo']

    def validate_yili(self, value):
        if len(value)==4:
            return value
        else:
            raise serializers.ValidationError({'error': 'Mashinaning Yili Oxiri 4ta belgidan utmaydi'})


class AvtoGetSer(serializers.ModelSerializer):
    model = ModelSer()
    rusum = RusumSer()
    photo = PhotoSer(many=True)
    shahar = ShaharSer()

    class Meta:
        model = Avto
        fields = ['id', 'model', 'rusum', 'yili', 'savdolashuv', 'yurgani',
        'uzatma', 'photo', 'xolati', 'yeyishi', 'karobka', 'rang',
        'kraska_holati', 'shahar', 'narhi', 'valyuta', 'dvigatel',
        'user', 'data', 'yana']
