from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ph_number = models.CharField(("Phone number"), max_length=50)
