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
    quantity = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
