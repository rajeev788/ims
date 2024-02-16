

from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import*
from .serializer2 import *
from rest_framework import status
from rest_framework.views import APIView #bot api view and genricapiview can be  inherited
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.decorators import permission_classes
from core.permissions import CustomModelPermission
from rest_framework.permissions import IsAuthenticated
from core.permissions import CustomModelPermission
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class Supplier(generics.ListCreateAPIView):
    queryset_model=Suppliers
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['supplier_name']
    search_fields=['supplier_name','supplier_email']
    permission_classes=[IsAuthenticated,CustomModelPermission]
    queryset=Suppliers.objects.all()
    serializer_class=SuppliersSerializer
        
        
class SupplierID(GenericAPIView):
    queryset_model=Suppliers
    permission_classes=[IsAuthenticated,CustomModelPermission]
    def get_supplier_object(self,pk):
        suppliers=get_object_or_404(Suppliers,pk=pk)
        return suppliers

    def get(self,request,pk):
        suppliers=self.get_supplier_object(pk)
        serrializer=SuppliersSerializer(suppliers)
        return Response(serrializer.data)
    def put(self,request,pk):
        suppliers=self.get_supplier_object(pk)
        serializer=SuppliersSerializer(suppliers,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated")
        else:
            return Response(serializer.errors)
        
    def patch(self,request,pk):
        suppliers=self.get_supplier_object(pk)
        serializers= SuppliersSerializer(suppliers,data=request.data,partial=True)
        if serializers.is_valid():
            return Response("data updated")
        else:
            return(serializers.errors)
        
    def delete(self,request,pk):
        suppliers = self.get_supplier_object(pk)
        suppliers.delete()
        return Response('data deleted!')
    


class CategoryAPi(generics.ListCreateAPIView,GenericAPIView):
    queryset_model=Categories
    permission_classes=[IsAuthenticated,CustomModelPermission]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['category_name']
    search_fields=['category_name']
    queryset=Categories.objects.all()
    serializer_class=CategoriesSerializer

class CategoryidAPI(GenericAPIView):
    queryset_model=Categories
    permission_classes=[IsAuthenticated,CustomModelPermission]
    def get_category_object(self,pk):
        categories=get_object_or_404(Categories,pk=pk)
        return categories
    
    def get(self,request,pk):
        categories=self.get_category_object(pk)
        serializer=CategoriesSerializer(categories)
        return Response(serializer.data)
    
    def put(self,request,pk):
        Categories=self.get_category_object(pk)
        serializers=CategoriesSerializer(Categories,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response("data updated")
        else:
            return Response(serializers.errors)
        
    def patch(self,request,pk):
        categories=self.get_category_object(pk)
        serializers=CategoriesSerializer(categories,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response("data updated")
        else:
            return Response(serializers.errors)
        
    def delete(self,request,pk):
        suppliers=self.get_category_object(pk)
        suppliers.delete()
        return Response("data deleted")
    

class ProductApi(generics.ListCreateAPIView):
    
    queryset_model=Product
    permission_classes=(IsAuthenticated,CustomModelPermission)
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['supplier_id','category_id']
    search_fields=['product_description','product_name']
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
        
class ProductIdApi(GenericAPIView):
    queryset_model=Product
    permission_classes=[IsAuthenticated,CustomModelPermission]
    def get_product_objects(self,pk):
        product=get_object_or_404(Product,pk=pk)
        return product
    
    def get(self,request,pk):
        product=self.get_product_objects(pk)
        serializers=ProductSerializer(product)
        return Response(serializers.data)
    
    def patch(self, request,pk):
        product=self.get_product_objects(pk)
        serializers=ProductSerializer(product,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response("data updated")
        else:
            return Response(serializers.errors)
        
    def put(self,request,pk):
        product=self.get_product_objects(pk)
        serializers=ProductSerializer(product,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response("data updated")
        else:
            return Response(serializers.errors)
        
    def delete(self,request, pk):
        product=self.get_product_objects(pk)
        product.delete()
        return Response("data deleted")
    


class Product_trackApi(generics.ListCreateAPIView):
    queryset_model=Product_track
    permission_classes=[IsAuthenticated,CustomModelPermission]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['product_id']
    # search_fields=['product_id']
    queryset=Product_track.objects.all()
    serializer_class=Product_trackSerializer

class Product_trackIdApi(GenericAPIView):
    queryset_model=Product_track
    permission_classes=[IsAuthenticated,CustomModelPermission]
    def get_product_track_object(self,pk):
        product=get_object_or_404(Product_track,pk=pk)
        return product
    

    def get(self,request,pk):
        product=self.get_product_track_object(pk)
        serializers=Product_trackSerializer(product)
        return Response(serializers.data)
    
    def put(self,request,pk):
        product=self.get_product_track_object(pk)
        serializers=Product_trackSerializer(product,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response("data updated")
        else:
            return Response(serializers.errors)
        

    def put(self,request,pk):
        product=self.get_product_track_object(pk)
        serializers=Product_trackSerializer(product,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response("data updated")
        else:
            return Response(serializers.errors)
        
    def delete(self,request,pk):
        product=self.get_product_track_object(pk)
        product.delete()
        return Response("data deleted")

class Product_OrderApi(generics.ListCreateAPIView):
    queryset_model=Product_Order
    permission_classes=[IsAuthenticated,CustomModelPermission]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['product_name','supplier_id','category_id']
    search_fields=['product_name']
    queryset=Product_Order.objects.all()
    serializer_class=Product_OrderSerializer

        
class Product_OrderIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=Product_Order
    permission_classes=[IsAuthenticated,CustomModelPermission]
    queryset=Product_Order.objects.all()
    serializer_class=Product_OrderSerializer