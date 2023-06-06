from django.db import models

# from sell.models import *


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(("First name"), max_length=50)
    last_name = models.CharField(("Last name"), max_length=50)
    p_num = models.CharField(("Phone number"), max_length=20)
    debt = models.IntegerField(("Debt"), null=True, blank=True, default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Payment(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    payment = models.IntegerField()

    def __str__(self):
        return f"{self.payment} | {self.customer}"