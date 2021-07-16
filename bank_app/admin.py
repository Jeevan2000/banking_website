from django.contrib import admin
from .models import NewCustomer,TransactionHistory

# Register your models here.
admin.site.register(NewCustomer)
admin.site.register(TransactionHistory)