from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import *
from . serializer import *

# Create your views here.
class DealerViewSet(ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer