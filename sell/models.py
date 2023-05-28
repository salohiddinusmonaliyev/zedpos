from clients.models import Client

from django.db import models

from product.models import Product

# Create your models here.
class Sell(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    time = models.DateTimeField()
    total_price = models.IntegerField(null=True, blank=True, default=0)
    description = models.TextField(null=True, blank=True)
    worker = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

class SellItem(models.Model):
    sell_id = models.ForeignKey(Sell, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    discount = models.IntegerField(null=True, default=0)
    date = models.DateTimeField(null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.product.name} {self.sell_id.time}"



class ClientPay(models.Model):
    datatime = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sell_id = models.ForeignKey(Sell, on_delete=models.CASCADE)
    payment = models.IntegerField()
    comment = models.CharField(max_length=200)


class CostCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cost(models.Model):
    worker = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    reason = models.ForeignKey(CostCategory, on_delete=models.CASCADE)
    date = models.DateTimeField()
    money = models.IntegerField()

    def __str__(self):
        return f"{self.worker.username} | {self.money}"


class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, default=None)
    sell_id = models.ForeignKey(Sell, on_delete=models.CASCADE)
    payment = models.IntegerField()
    comment = models.CharField(max_length=200)
