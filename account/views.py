from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import RegisterSerializer, LoginSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User


class RegisterView(APIView):
   
   def post(self, request):

      try:
         data = request.data
         serializer = RegisterSerializer(data=data)

         if not serializer.is_valid():
            return Response({
               'data' : serializer.errors,
               'messeage': 'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

         serializer.save()

         return Response({
            'data': {},
            'messeage' : 'your account is created'
         }, status= status.HTTP_201_CREATED)

      except Exception as e:
         print(e)
         return Response({
               'data' : {},
               'messeage': 'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):

   def post(self, request):
      try:
         data = request.data
         serializer = LoginSerializer(data=data)

         if not serializer.is_valid():
            return Response({
               'data' : serializer.errors,
               'messeage': 'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

         response = serializer.get_jwt_token(serializer.data)

         return Response(response, status= status.HTTP_200_OK)

      except Exception as e:
         print(e)
         return Response({
               'data' : {},
               'messeage': 'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
      
