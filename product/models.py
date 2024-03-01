from django.db import models

from accounts.models import CustomUser
from dealer.models import Dealer

# Create your models here.


class Measure(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

class Product(models.Model):
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    arrival_price = models.IntegerField()
    price = models.IntegerField()
    measure = models.ForeignKey(Measure, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField(null=True)
    is_active = models.BooleanField(default=True)
    count = models.FloatField(null=True, blank=True, default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class AddProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    quantity = models.IntegerField(null=True)
    total_price = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.dealer_id.name
