
from .views import *
from django.urls import path
from django.contrib import admin


urlpatterns=[
    path('customers',CustomerApi.as_view()),
    path('customersId/<pk>',CustomerIdApi.as_view()),
    path('customer_orders',OrderApi.as_view()),
    path('customer_ordersId/<pk>',OrderIdApi.as_view()),
    path('shippingId/<pk>',ShippingIdApi.as_view()),
    path('shipping',ShippingApi.as_view()),
   
    
]
