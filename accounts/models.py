from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    status = (
        ("Unpaid", "Unpaid"),
        ("Paid", "Paid"),
    )
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    status = models.CharField(choices=status, max_length=100, default="Unpaid")
    shop_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.shop_name

class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ph_number = models.CharField(("Phone number"), max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

