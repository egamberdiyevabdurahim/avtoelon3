from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

from .models import User
from avto.models import Like, Avto
from .serializer import UserSer


class SignUp(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        user = User.objects.all()
        ser = UserSer(user, many=True)
        return Response({'data': ser.data})

    def post(self, request):
        #send sms via email
        ser = UserSer(data=request.data)
        if ser.is_valid():
            user = ser.save()
            send_mail(
                'Avto Elon Uz',
                'Assalomu Aleykum Avto Elon Uz Saytiga Obuna Bo\'lganingizdan minnatdormiz Xurmat Va Extirom Bilan Avto Elon Uz Jamoasi',
                settings.EMAIL_HOST_USER,
                [user.email, ]
            )
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


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)
        token = Token.objects.create(user=user)
        id = user.id
        return Response({'token': token.key, 'id':id})


class LikeAvto(APIView):
	def get(self, request, id):
		pass

	def post(self, request, id):
		avto = Avto.objects.get(id=id)
		like = Like.objects.filter(avto=avto).first()
		if Like.objects.filter(avto=avto).exists():
			like = Like.objects.filter(avto=avto).first()
			if request.user in like.user.all():
				like.user.remove(request.user)
				return Response({'deleted':'successfully'})
			like.user.add(request.user)
			return Response({'added':'successfully'})
		like = Like.objects.create(
				avto=avto
			)
		like.user.add(request.user)
		return Response({'added':'successfully'})