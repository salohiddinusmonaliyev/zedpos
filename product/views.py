from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializer import *


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = ProductSerializer(instance=instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class MeasureViewSet(ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer