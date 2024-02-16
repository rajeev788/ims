
# Create your views here.
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.permissions import CustomModelPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
# Create your views here.

class AccountingApi(generics.ListCreateAPIView,GenericAPIView):
    queryset_model=Accounting
    permission_classes=[IsAuthenticated,CustomModelPermission]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['transactions_type']
    # search_fields=[]
    queryset=Accounting.objects.all()
    serializer_class=AccountingSerializer
    # def get(self, request):
    #     accounting=Accounting.objects.all()
    #     serializers=AccountingSerializer(accounting,many=True)
    #     return Response(serializers.data)
    
    # def post(self, request):
    #     serializers=AccountingSerializer(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response("data created")
    #     else:
    #         return Response(serializers.errors)

class AccountingIdApi(GenericAPIView):
    queryset_model=Accounting
    permission_classes=[IsAuthenticated,CustomModelPermission]
    def get_accounting_object(self, pk):
        accounting=get_object_or_404(Accounting,pk=pk)
        return accounting
    
    def get(self ,request, pk):
        accounting =self.get_accounting_object(pk)
        serializers=AccountingSerializer(accounting)
        return Response(serializers.data)
    
    def patch(self ,request, pk):
        accounting =self.get_accounting_object(pk)
        serializers=AccountingSerializer(accounting,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response("data updated")
        else:
            return Response(serializers.errors)
    def put(self ,request, pk):
        accounting =self.get_accounting_object(pk)
        serializers=AccountingSerializer(accounting,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response("data updated")
        else:
            return Response(serializers.errors)
    def delete(self,request,pk):
        accounting=self.get_accounting_object(pk)
        accounting.delete()
        return Response("data deleted")
    