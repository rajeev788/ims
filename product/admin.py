from django.contrib import admin


from .models import *

# admin.site.register(Suppliers)
# admin.site.register(Categories)
# admin.site.register(Product)
# admin.site.register(Product_track)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields=('product_name',)
    list_display=('product_name','product_unit_price','product_description','quatity_on_hand',)
    list_per_page=10
    list_filter=('category_id',)
    
    autocomplete_fields=('category_id','supplier_id',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields=('category_name',)
    list_display=('category_name','category_description',)
    list_per_page=10
    list_filter=("category_name",)


@admin.register(Product_track)
class Product_trackAdmin(admin.ModelAdmin):
    list_per_page=10
    autocomplete_fields=('product_id',)
    # list_filter=()    
    list_display=('product_id','product_in','product_out','opening_numbers_of_product','closing_number_of_products',)

@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    search_fields=('supplier_name',)
    list_per_page=10
    list_display=('supplier_name','supplier_email',)

@admin.register(Product_Order)
class Product_OrderAdmin(admin.ModelAdmin):
  
    list_per_page=10
    list_display=('supplier_id','category_id','product_name',)