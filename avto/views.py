from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

from User.models import User
from User.serializer import UserSer
from .models import (Davlat, Viloyat, Shahar, Model, Rusum, Photo, Avto)
from .serializer import (DavlatSer, ViloyatSer, ShaharSer, ModelSer, RusumSer,
                        PhotoSer, AvtoSer,
                        AvtoGetSer)


class AllApiList(APIView):
    def get(self, request):
        davlat = Davlat.objects.all()
        viloyat = Viloyat.objects.all()
        shahar = Shahar.objects.all()
        model = Model.objects.all()
        rusum = Rusum.objects.all()
        photo = Photo.objects.all()
        avto = Avto.objects.all()
        user = User.objects.all()
        davlatser = DavlatSer(davlat, many=True)
        viloyatser = ViloyatSer(viloyat, many=True)
        shaharser = ShaharSer(shahar, many=True)
        modelser = ModelSer(model, many=True)
        rusumser = RusumSer(rusum, many=True)
        photoser = PhotoSer(photo, many=True)
        avtoser = AvtoSer(avto, many=True)
        userser = UserSer(user, many=True)
        return Response((davlatser.data, viloyatser.data, shaharser.data,
            modelser.data, rusumser.data, photoser.data, avtoser.data, userser.data))


class DavlatApiList(APIView):
    def get(self, request):
        davlat = Davlat.objects.all()
        ser = DavlatSer(davlat, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = DavlatSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class DavlatApiDetail(APIView):
    def get(self, request, id):
        davlat = Davlat.objects.get(id=id)
        ser = DavlatSer(davlat)
        return Response(ser.data)

    def delete(self, request, id):
        davlat = Davlat.objects.get(id=id)
        davlat.delete()
        return Response({'message': 'deleted successfully'})

    def put(self, request, id):
        davlat = Davlat.objects.get(id=id)
        ser = DavlatSer(data=request.data, instance=davlat)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        davlat = Davlat.objects.get(id=id)
        ser = DavlatSer(data=request.data, instance=davlat, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class ViloyatApiList(APIView):
    def get(self, request):
        davlat = Viloyat.objects.all()
        ser = ViloyatSer(davlat, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = ViloyatSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class ViloyatApiDetail(APIView):
    def get(self, request, id):
        davlat = Viloyat.objects.get(id=id)
        ser = ViloyatSer(davlat)
        return Response(ser.data)

    def delete(self, request, id):
        davlat = Viloyat.objects.get(id=id)
        davlat.delete()
        return Response({'message': 'deleted successfully'})

    def put(self, request, id):
        davlat = Viloyat.objects.get(id=id)
        ser = ViloyatSer(data=request.data, instance=davlat)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        davlat = Viloyat.objects.get(id=id)
        ser = ViloyatSer(data=request.data, instance=davlat, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class ShaharApiList(APIView):
    def get(self, request):
        davlat = Shahar.objects.all()
        ser = ShaharSer(davlat, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = ShaharSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class ShaharApiDetail(APIView):
    def get(self, request, id):
        davlat = Shahar.objects.get(id=id)
        ser = ShaharSer(davlat)
        return Response(ser.data)

    def delete(self, request, id):
        davlat = Shahar.objects.get(id=id)
        davlat.delete()
        return Response({'message': 'deleted successfully'})

    def put(self, request, id):
        davlat = Shahar.objects.get(id=id)
        ser = ShaharSer(data=request.data, instance=davlat)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        davlat = Shahar.objects.get(id=id)
        ser = ShaharSer(data=request.data, instance=davlat, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class ModelApiList(APIView):
    def get(self, request):
        davlat = Model.objects.all()
        ser = ModelSer(davlat, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = ModelSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class ModelApiDetail(APIView):
    def get(self, request, id):
        davlat = Model.objects.get(id=id)
        ser = ModelSer(davlat)
        return Response(ser.data)

    def delete(self, request, id):
        davlat = Model.objects.get(id=id)
        davlat.delete()
        return Response({'message': 'deleted successfully'})

    def put(self, request, id):
        davlat = Model.objects.get(id=id)
        ser = ModelSer(data=request.data, instance=davlat)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        davlat = Model.objects.get(id=id)
        ser = ModelSer(data=request.data, instance=davlat, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class RusumApiList(APIView):
    def get(self, request):
        davlat = Rusum.objects.all()
        ser = RusumSer(davlat, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = RusumSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class RusumApiDetail(APIView):
    def get(self, request, id):
        davlat = Rusum.objects.get(id=id)
        ser = RusumSer(davlat)
        return Response(ser.data)

    def delete(self, request, id):
        davlat = Rusum.objects.get(id=id)
        davlat.delete()
        return Response({'message': 'deleted successfully'})

    def put(self, request, id):
        davlat = Rusum.objects.get(id=id)
        ser = RusumSer(data=request.data, instance=davlat)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        davlat = Rusum.objects.get(id=id)
        ser = RusumSer(data=request.data, instance=davlat, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class PhotoApiList(APIView):
    def get(self, request):
        davlat = Photo.objects.all()
        ser = PhotoSer(davlat, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = PhotoSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class PhotoApiDetail(APIView):
    def get(self, request, id):
        davlat = Photo.objects.get(id=id)
        ser = PhotoSer(davlat)
        return Response(ser.data)

    def delete(self, request, id):
        davlat = Photo.objects.get(id=id)
        davlat.delete()
        return Response({'message': 'deleted successfully'})

    def put(self, request, id):
        davlat = Photo.objects.get(id=id)
        ser = PhotoSer(data=request.data, instance=davlat)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        davlat = Photo.objects.get(id=id)
        ser = PhotoSer(data=request.data, instance=davlat, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class AvtoApiList(APIView):
    parser_classes = [MultiPartParser, JSONParser]
    def get(self, request):
        avto = Avto.objects.all()
        ser = AvtoGetSer(avto, many=True)
        return Response(ser.data)

    def post(self, request):
        photo_list = request.data.getlist('photo', [])
        ser = AvtoSer(data=request.data)
        if ser.is_valid():
            news = ser.save()
            for x in photo_list:
                p = Photo.objects.create(photo=x)
                news.photo.add(p)
            return Response(ser.data)
        return Response(ser.errors)


class AvtoApiDetail(APIView):
    parser_classes = [MultiPartParser, JSONParser]
    def get(self, request, id):
        try:
            avto = Avto.objects.get(id=id)
            ser = AvtoSer(avto)
            return Response(ser.data)
        except:
            return Response({'error': 'Bunday Mashina Mavjud Emas'})

    def delete(self, request, id):
        avto = Avto.objects.get(id=id)
        avto.delete()
        return Response({'message': 'deleted successfully'})

    def put(self, request, id):
        avto = Avto.objects.get(id=id)
        ser = AvtoSer(data=request.data, instance=avto)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        avto = Avto.objects.get(id=id)
        ser = AvtoSer(data=request.data, instance=avto, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
