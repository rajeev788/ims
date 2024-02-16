from .models import *
from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields=['id','name']
        model=Group
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=['email','password','groups']
        model= User