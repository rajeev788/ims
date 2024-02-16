from django.contrib import admin


# Register your models here.
from .models import *
# admin.site.register(Customer)
# admin.site.register(Order)


@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display=('name','email',)
    list_per_page=10
    search_fields=('name',)


@admin.register(Customer_Order)
class OrderAdmin(admin.ModelAdmin):
    list_per_page=10
    list_display=('customer_id','product_id','total','payment_status',)
    autocomplete_fields=('customer_id','product_id',)
    # list_filter=()
@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display=('shipping_status',"customer_id",)
   