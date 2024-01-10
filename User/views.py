from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

from .models import User
from .serializer import UserSer


class SignUp(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        user = User.objects.all()
        ser = UserSer(user, many=True)
        return Response({'data': ser.data})


    def post(self, request):
        ser = UserSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class Change(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request, id):
        user = User.objects.filter(id=id).first()
        ser = UserSer(user)
        return Response(ser.data)

    def delete(self, request, id):
        user = User.objects.filter(id=id).first()
        user.delete()
        return Response({'message': 'User successfully deleted'})

    def put(self, request, id):
        user = User.objects.filter(id=id).first()
        ser = UserSer(data=request.data, instance=user)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, id):
        user = User.objects.filter(id=id).first()
        ser = UserSer(data=request.data, instance=user, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)