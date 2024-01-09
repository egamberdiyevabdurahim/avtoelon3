from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

from .models import Davlat, Viloyat, Shahar, Model, Rusum, Karobka, Rang, Yeyishi, Photo, Avto
from .serializer import DavlatSer, ViloyatSer, ShaharSer, ModelSer, RusumSer, KarobkaSer, RangSer, YeyishiSer, PhotoSer, AvtoSer, AvtoGetSer


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


class KarobkaApiList(APIView):
    def get(self, request):
        davlat = Karobka.objects.all()
        ser = KarobkaSer(davlat, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = KarobkaSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class KarobkaApiDetail(APIView):
    def get(self, request, id):
        davlat = Karobka.objects.get(id=id)
        ser = KarobkaSer(davlat)
        return Response(ser.data)

    def delete(self, request, id):
        davlat = Karobka.objects.get(id=id)
        davlat.delete()
        return Response({'message': 'deleted successfully'})

    def put(self, request, id):
        davlat = Karobka.objects.get(id=id)
        ser = KarobkaSer(data=request.data, instance=davlat)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        davlat = Karobka.objects.get(id=id)
        ser = KarobkaSer(data=request.data, instance=davlat, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class RangApiList(APIView):
    def get(self, request):
        davlat = Rang.objects.all()
        ser = RangSer(davlat, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = RangSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class RangApiDetail(APIView):
    def get(self, request, id):
        davlat = Rang.objects.get(id=id)
        ser = RangSer(davlat)
        return Response(ser.data)

    def delete(self, request, id):
        davlat = Rang.objects.get(id=id)
        davlat.delete()
        return Response({'message': 'deleted successfully'})

    def put(self, request, id):
        davlat = Rang.objects.get(id=id)
        ser = RangSer(data=request.data, instance=davlat)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        davlat = Rang.objects.get(id=id)
        ser = RangSer(data=request.data, instance=davlat, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class YeyishiApiList(APIView):
    def get(self, request):
        davlat = Yeyishi.objects.all()
        ser = YeyishiSer(davlat, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = YeyishiSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class YeyishiApiDetail(APIView):
    def get(self, request, id):
        davlat = Yeyishi.objects.get(id=id)
        ser = YeyishiSer(davlat)
        return Response(ser.data)

    def delete(self, request, id):
        davlat = Yeyishi.objects.get(id=id)
        davlat.delete()
        return Response({'message': 'deleted successfully'})

    def put(self, request, id):
        davlat = Yeyishi.objects.get(id=id)
        ser = YeyishiSer(data=request.data, instance=davlat)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        davlat = Yeyishi.objects.get(id=id)
        ser = YeyishiSer(data=request.data, instance=davlat, partial=True)
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
        avto = Avto.objects.get(id=id)
        ser = AvtoSer(avto)
        return Response(ser.data)

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
