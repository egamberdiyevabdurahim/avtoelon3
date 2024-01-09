from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

from .models import User
# from .serializer import UserSer
#
#
# class SignUp(APIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     def get(self, request):
#         user = User.objects.all()
#         if user:
#             ser = UserSer(user, many=True)
#             return Response({'data': ser.data})
#         return Response({'message': 'Sizda Hali Userlar Yoq'})
#
#     def post(self, request):
#         ser = UserSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
