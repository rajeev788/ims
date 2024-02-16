from rest_framework import serializers
from .models import *

class SupplierName(serializers.RelatedField):
    queryset=Suppliers.objects.all()
    def to_representation(self, value):
        return value.supplier_name
    def to_internal_value(self, data):
        supplier_id,_=Suppliers.objects.get_or_create(supplier_name=data)
        return supplier_id

class CategoryName(serializers.RelatedField):
    queryset=Categories.objects.all()
    def to_representation(self, value):
        return value.category_name
    def to_internal_value(self, data):
        category_id,_=Categories.objects.get_or_create(category_name=data)
        return category_id
    

class ProductName(serializers.RelatedField):
    queryset=Product.objects.all()
    def to_representation(self, value):
        return value.product_name
    def to_internal_value(self, data):
        product_id,_=Product.objects.get_or_create(product_name=data)
        return product_id
    
class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
         fields="__all__"
         model=Suppliers

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
         fields="__all__"
         model=Categories

class ProductSerializer(serializers.ModelSerializer):
     supplier_id=SupplierName()
     category_id=CategoryName()
     class Meta:
    
         fields='__all__'
         model=Product

class Product_trackSerializer(serializers.ModelSerializer):
     product_id=ProductName()
     
     class Meta:
          fields="__all__"
          model=Product_track

class Product_OrderSerializer(serializers.ModelSerializer):
          supplier_id=SupplierName()
          category_id=CategoryName()
          class Meta:
            fields="__all__"
            model=Product_Order