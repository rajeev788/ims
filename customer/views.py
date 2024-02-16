

# Create your views here.
from django.shortcuts import render,get_object_or_404
from rest_framework import status
from .serializer1 import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import *
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.permissions import CustomModelPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Cryour views here.
class CustomerApi(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
   queryset_model=Customer
   permission_classes=[IsAuthenticated,CustomModelPermission]
   filter_backends=[DjangoFilterBackend,filters.SearchFilter]
   filterset_fields=['name']
   search_fields=['name',"email"]
   queryset=Customer.objects.all()
   serializer_class=CustomerSerializer
   def get(self,request):
       return self.list(request)
   def post(self,request):
       return self.create(request)

   
class CustomerIdApi(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,GenericAPIView):
    queryset_model=Customer
    permission_classes=[IsAuthenticated,CustomModelPermission]
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer #thsi mixins is shortcut ,insteed of making individual api
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
        
    def put(self,request,pk,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,pk,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)




class OrderApi(generics.ListCreateAPIView):
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['payment_status','customer_id']
    # search_fields=['',]
    queryset_model=Customer_Order
    permission_classes=[IsAuthenticated,CustomModelPermission]
    queryset=Customer_Order.objects.all()
    
    serializer_class=Customer_OrderSerializer
    
    #     order=Order.objects.all()
    #     serializers=OrderSerializer(order,many=True)
    #     return Response(serializers.data)
    # def post(self, request):
    #     serializers=OrderSerializer(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response("data created")
    #     else:
    #         return Response(serializers.errors)

class OrderIdApi(generics.RetrieveUpdateDestroyAPIView,GenericAPIView):

    queryset_model=Customer_Order
    permission_classes=[IsAuthenticated,CustomModelPermission]
    
    queryset=Customer_Order.objects.all()
    serializer_class=Customer_OrderSerializer
    # def get_order_object(self, pk):
    #     order=get_object_or_404(Order,pk=pk)
    #     return order
    
    # def get(self ,request, pk):
    #     order =self.get_order_object(pk)
    #     serializers=OrderSerializer(order)
    #     return Response(serializers.data)
    # def patch(self ,request, pk):
    #     order =self.get_order_object(pk)
    #     serializers=OrderSerializer(order,data=request.data,partial=True)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response("data updated")
    #     else:
    #         return Response(serializers.errors)
    # def put(self ,request, pk):
    #     order =self.get_order_object(pk)
    #     serializers=OrderSerializer(order,data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response("data updated")
    #     else:
    #         return Response(serializers.errors)
        
    # def delete(self,request,pk):
    #     order=self.get_order_object(pk)
    #     order.delete()
    #     return Response("data deleted")

class ShippingApi(generics.ListCreateAPIView):
        queryset_model=Shipping
        permission_classes=[IsAuthenticated,CustomModelPermission]
        filter_backends=[DjangoFilterBackend,filters.SearchFilter]
        filterset_fields=['customer_id','shipping_status']
        search_fields=['shipping_status']
        serializer_class=ShippingSerializer
        queryset=Shipping.objects.all()
        # filterset_fields=['customer_id','shipping_status']
class ShippingIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=Shipping
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=ShippingSerializer
    queryset=Shipping.objects.all()