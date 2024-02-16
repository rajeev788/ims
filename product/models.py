from django.db import models



# Create your models here.



class Suppliers(models.Model):
    supplier_name=models.CharField(max_length=300)
    supplier_contact=models.IntegerField()
    supplier_email=models.EmailField(blank=True,null=True)
    def __str__(self):
        return self.supplier_name

class Categories(models.Model):
    category_name=models.CharField(max_length=300)
    category_description=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name=models.CharField(max_length=300,)
    product_description= models.TextField()
    product_unit_price=models.IntegerField()
    quatity_on_hand=models.IntegerField()
    supplier_id=models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    category_id=models.ForeignKey(Categories,on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name


class Product_track(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_in=models.IntegerField()
    product_out=models.IntegerField()
    opening_numbers_of_product=models.IntegerField()
    closing_number_of_products=models.IntegerField()
   

class Product_Order(models.Model):
    supplier_id=models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    category_id=models.ForeignKey(Categories,on_delete=models.CASCADE)
    order_number=models.IntegerField()
    product_name=models.CharField(max_length=300)