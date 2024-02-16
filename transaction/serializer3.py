from rest_framework import serializers
from .models import *
from product.serializer2 import ProductName

class Inventory_TransactionSerializer(serializers.ModelSerializer):
    class Meta:
         fields="__all__"
         model=Inventory_Transaction

class Inventory_transaction_detailsSerializer(serializers.ModelSerializer):
    product_id=ProductName()
   
    class Meta:
         fields="__all__"
         model=Inventory_transaction_details

# class TransactionName(serializers.RelatedField):
#     queryset=Inventory_Transaction.objects.all()
#     def to_representation(self, value):
#         return value.supplier_name
#     def to_internal_value(self, data):
#         transaction_id,_=Inventory_Transaction.objects.get_or_create(=data)
#         return supplier_id