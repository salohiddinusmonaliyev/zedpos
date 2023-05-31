from django.db import models

from dealer.models import Dealer
from product.models import Product


# Create your models here.
class Warehouse(models.Model):
    STATUS = (
        ('Paid', "Paid"),
        ('Unpaid', 'Unpaid'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    dealer_id = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField(null=True)
    total_price = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.dealer_id.name
