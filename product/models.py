from django.db import models

from dealer.models import Dealer

# Create your models here.


class Measure(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    incoming_price = models.IntegerField()
    price = models.IntegerField()
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    dealer_id = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField(null=True)
    size = models.CharField(max_length=50)
    total_price = models.IntegerField()


    def __str__(self):
        return self.dealer_id.name
