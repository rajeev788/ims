from django.db import models


# Create your models here

from transaction.models import Inventory_Transaction
# Create your models here.

from product.models import Product

Transactions_type=[('Purchase','Purchase'),('Sales','Sales'),('Adjustment','Adjustment')]
# Create your models here.
class Accounting(models.Model):
   
    transactions_id=models.ForeignKey(Inventory_Transaction,on_delete=models.CASCADE)
    transactions_type=models.CharField(max_length=300,choices=Transactions_type,default='Sales')
    transaction_date=models.DateField()
    debit_amt=models.IntegerField(null=True,blank=True)
    credit_amt=models.IntegerField(null=True,blank=True)