from rest_framework import serializers
from .models import *

class AccountingSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=Accounting