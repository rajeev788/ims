from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Inventory_Transaction)
# admin.site.register(Inventory_transaction_details)

@admin.register(Inventory_Transaction)
class Inventory_TransactionAdmin(admin.ModelAdmin):
    list_display=('transaction_type','transaction_type',)
    list_per_page=10
    list_filter=('transaction_type',)


@admin.register(Inventory_transaction_details)
class Inventory_transaction_detailsAdmin(admin.ModelAdmin):
    #   list_display=('product_id','transaction_id')
      list_per_page=10
      list_display=('product_id',)
      autocomplete_fields=('product_id',)
     
