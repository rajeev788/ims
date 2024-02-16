from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from .serializer4 import *
from core.permissions import CustomModelPermission
# Create your views here.
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email,password=password)
    if user == None:
        return Response('Email or Password is Invalid!')
    else:
        token , _ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated,CustomModelPermission])
def logout(request):
    request.user.auth_token.delete()
    return Response('logout successful')

@api_view(['POST'])
@permission_classes([IsAuthenticated,CustomModelPermission])

def register(request):
   password=request.data.get('password')
   email=request.data.get('email')
   hash_password=make_password(password)
   request.data['password']=hash_password 
   serializers=UserSerializer(data=request.data)
   if serializers.is_valid():
       serializers.save()
       return Response("user created") 
   else:
       return Response(serializers.errors)

class GroupApi(generics.ListCreateAPIView,GenericAPIView):
    queryset_model=Group
    permission_classes=[IsAuthenticated,CustomModelPermission]
    queryset_model =Group
    permission_classes=(IsAuthenticated,IsAdminUser)
    queryset=Group.objects.all()
    serializer_class=GroupSerializer

