from rest_framework.serializers import ModelSerializer

from .models import *

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class WarehouseSerializer(ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"

class MeasureSerializer(ModelSerializer):
    class Meta:
        model = Measure
        fields = "__all__"

