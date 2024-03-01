from django.db import models

from accounts.models import CustomUser


# from sell.models import *


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(("First name"), max_length=50)
    last_name = models.CharField(("Last name"), max_length=50)
    p_num = models.CharField(("Phone number"), max_length=20)
    debt = models.IntegerField(("Debt"), null=True, blank=True, default=0)
    count = models.IntegerField(null=True)
    sale = models.IntegerField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class CustomerPayment(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    paymnet = models.IntegerField()
    comment = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.customer.first_name