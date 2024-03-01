from django.db import models

from accounts.models import CustomUser


# Create your models here.
class Dealer(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=50, null=True)
    debt = models.IntegerField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True)
    payment = models.IntegerField()
    date = models.DateField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
