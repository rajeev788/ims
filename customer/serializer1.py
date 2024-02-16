from .models import *
from rest_framework import serializers


class CustomerName(serializers.RelatedField):
    queryset=Customer.objects.all()
    def to_representation(self, value):
        return value.name
    def to_internal_value(self, data):
        customer_id,_=Customer.objects.get_or_create(name=data)
        return customer_id


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=Customer

class Customer_OrderSerializer(serializers.ModelSerializer):
         customer_id=CustomerName()
         product_id=ProductName()
         class Meta:
          fields="__all__"
          model=Customer_Order

class ShippingSerializer(serializers.ModelSerializer):
    customer_id=CustomerName()
    class Meta:
         fields="__all__"
         model=Shipping


