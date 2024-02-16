from django.contrib import admin


# Register your models here.
from .models import *

@admin.register(Accounting)
class AccountingAdmin(admin.ModelAdmin):
    # search_fields=('transaction_type','transaction_date',)
    list_display=('transactions_id','transactions_type','transaction_date','debit_amt','credit_amt',)
    list_per_page=10
 

   

