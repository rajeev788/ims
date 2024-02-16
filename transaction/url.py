from .views import *
from django.urls import path

urlpatterns=[
    path('inventory_transactions',Inventory_TransactionApi.as_view()),
    path('inventoy_transactionsId/<pk>',Inventory_TransactionIdApi.as_view()),
    path('inventory_transactions_details',Inventory_transaction_detailsApi.as_view()),
    path('inventory_transactions_detailsId/<pk>',Inventory_transaction_detailsIdApi.as_view()),
]