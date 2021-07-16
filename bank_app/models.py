from django.db import models

# Create your models here.
class NewCustomer(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    balance=models.IntegerField()
    branchname=models.CharField(max_length=100)
    ifsc=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    scheme=models.CharField(max_length=100)

class TransactionHistory(models.Model):
    sender_id=models.IntegerField()
    sender_name=models.CharField(max_length=100)
    receiver_id=models.IntegerField()
    receiver_name=models.CharField(max_length=100)
    amount_fee=models.IntegerField()
    time=models.CharField(max_length=100)

    