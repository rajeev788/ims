
from .views import *
from django.urls import path
from django.contrib import admin

urlpatterns=[
    path('accountings',AccountingApi.as_view()),
    path('accountingsId/<pk>',AccountingIdApi.as_view()),
]
