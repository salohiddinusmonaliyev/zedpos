from django.contrib.auth.models import User

from accounts.models import Worker, CustomUser
from clients.models import Client

from django.db import models

from product.models import Product

# Create your models here.
class Sell(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    time = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True, default=0)
    checkout = models.BooleanField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    # paid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}"

class SellItem(models.Model):
    sell_id = models.ForeignKey(Sell, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(null=True)
    date = models.DateTimeField(null=True, blank=True)
    discount = models.IntegerField(null=True, default=0)
    total_price = models.IntegerField(null=True)
    quantity = models.FloatField()
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.id} {self.sell_id.time}"


class CostCategory(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name

class Cost(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(CostCategory, on_delete=models.CASCADE)
    date = models.DateTimeField()
    cost = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.cost}"

class Return(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    sellitem = models.ForeignKey(SellItem, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.IntegerField(null=True)
    quantity = models.FloatField(null=True)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.customer.first_name

