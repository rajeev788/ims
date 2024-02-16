from django.db import models



from product.models import Product
# Create your models here.

type=[('sales','sales'),('purchase','purchase')]
class Inventory_Transaction(models.Model):
    transaction_type=models.CharField(max_length=300,choices=type)
    transaction_date=models.DateField()
 
class Inventory_transaction_details(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    unit_price=models.IntegerField()
    total_price=models.IntegerField()
  
    notes=models.TextField(null=True)
    transaction_id=models.ForeignKey(Inventory_Transaction,on_delete=models.CASCADE)
