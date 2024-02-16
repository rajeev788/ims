
# Create your views here.
from django.shortcuts import render,get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from .serializer3 import *
from rest_framework.response import Response
from .models import *
from rest_framework.generics import GenericAPIView
from core.permissions import CustomModelPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

# Create your views here.
class Inventory_TransactionApi(generics.ListCreateAPIView):
    queryset_model=Inventory_Transaction
    permission_classes=[IsAuthenticated,CustomModelPermission]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['transaction_type']
    search_fields=['transaction_date']
    queryset=Inventory_Transaction.objects.all()
    serializer_class=Inventory_TransactionSerializer
        
class Inventory_TransactionIdApi(GenericAPIView):
    queryset_model=Inventory_Transaction
    permission_classes=[IsAuthenticated,CustomModelPermission]
    def get_inventory_transaction_object(self,pk):
        inventory_transaction=get_object_or_404(Inventory_Transaction,pk=pk)
        return inventory_transaction
    
    def get(self,request,pk):
        inventory_transaction=self.get_inventory_transaction_object(pk)
        serializers=Inventory_TransactionSerializer(inventory_transaction)
        return Response(serializers.data)
    
    def put(self,request,pk):
        inventory_transaction=self.get_inventory_transaction_object(pk)
        serializer=inventory_transaction(inventory_transaction,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated")
        else:
            return Response(serializer.errors)
        
    def put(self,request,pk):
        inventory_transaction=self.get_inventory_transaction_object(pk)
        serializer=inventory_transaction(inventory_transaction,data=request.data,partail=True)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated")
        else:
            return Response(serializer.errors)
    def delete(self,pk):
        inventory_transaction=self.get_inventory_transaction_object(pk)
        inventory_transaction.delete()
        return inventory_transaction    


class Inventory_transaction_detailsApi(generics.ListCreateAPIView):
    queryset_model=Inventory_transaction_details
    permission_classes=[IsAuthenticated,CustomModelPermission]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['product_id','transaction_id']
    # search_fields=['name']
    queryset=Inventory_transaction_details.objects.all()
    serializer_class=Inventory_transaction_detailsSerializer
        


class Inventory_transaction_detailsIdApi(GenericAPIView):
    queryset_model=Inventory_transaction_details
    permission_classes=[IsAuthenticated,CustomModelPermission]
    def get_inventory_transaction_details_object(self,pk):
        inventory_transaction_details=get_object_or_404(Inventory_transaction_details,pk=pk)
        return inventory_transaction_details
        

    def get(self,request,pk):
        inventory_transactions_details=self.get_inventory_transaction_details_object(pk)
        serializers=Inventory_transaction_detailsSerializer(inventory_transactions_details)
        return Response(serializers.data)
    
    def put(self,request,pk):
        inventory_transactions_details=self.get_inventory_transaction_details_object(pk)
        serializer=Inventory_transaction_detailsSerializer(inventory_transactions_details,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data created")
        else:
            return Response(serializer.errors)
        
        
    def patch(self,request,pk):
        inventory_transactions_details=self.get_inventory_transaction_details_object(pk)
        serializer=Inventory_transaction_detailsSerializer(inventory_transactions_details,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("data created")
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        inventory_transactions_details=self.get_inventory_transaction_details_object(pk)
        inventory_transactions_details.delete()
        return Response("data deleted")
      