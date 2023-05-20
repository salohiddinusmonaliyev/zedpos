from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ph_number = models.CharField(("Phone number"), max_length=50)
