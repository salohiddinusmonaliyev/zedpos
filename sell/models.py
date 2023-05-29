from clients.models import Client

from django.db import models

from product.models import Product

# Create your models here.
class Sell(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    time = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    discount = models.IntegerField(null=True, default=0)
    checkout = models.BooleanField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}"

class SellItem(models.Model):
    sell_id = models.ForeignKey(Sell, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.product.name} {self.sell_id.time}"


class CostCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cost(models.Model):
    reason = models.ForeignKey(CostCategory, on_delete=models.CASCADE)
    date = models.DateTimeField()
    money = models.IntegerField()

    def __str__(self):
        return f"{self.money}"


class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, default=None)
    sell_id = models.ForeignKey(Sell, on_delete=models.CASCADE)
    payment = models.IntegerField()
    time = models.DateTimeField(null=True, blank=True)
    comment = models.CharField(max_length=200)
