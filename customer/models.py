from django.db import models
from product.serializer2 import ProductName

from django.contrib.auth import get_user_model

# Create your models here.
from product.models import Product

status=[('paid','paid'),('notpaid','notpaid')]
shipping=[('shipped','shipped'),('not shipped','not shipped')]


class Customer(models.Model):
    name=models.CharField(max_length=300)
    contact=models.IntegerField()
    email=models.EmailField()
    addresss=models.CharField(max_length=300)
    def __str__(self):
        return self.name
    


class Shipping(models.Model):
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    shipping_status=models.CharField(max_length=300,choices=shipping)

class Customer_Order(models.Model):
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date=models.DateField()
    payment_status=models.CharField(max_length=300,choices=status)
    product_id =models.ForeignKey(Product,on_delete=models.CASCADE )
    unit_price=models.IntegerField()
    quantity=models.IntegerField()
    total=models.IntegerField()

 