from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns=[
    path('suppliers',Supplier.as_view()),
    path('suppliersId/<pk>',SupplierID.as_view()),
    path('categories',CategoryAPi.as_view()),
    path("categoriesId/<pk>",CategoryidAPI.as_view()),
    path('products',ProductApi.as_view()),
    path("productsId/<pk>",ProductIdApi.as_view()),
    path("products_track",Product_trackApi.as_view()),
    path("products_trackId/<pk>",Product_trackIdApi.as_view()),
    path("products_order",Product_OrderApi.as_view()),
    path("products_orderId/<pk>",Product_OrderIdApi.as_view()),


    
]