from rest_framework.serializers import ModelSerializer

from .models import *

class SellSerializer(ModelSerializer):
    class Meta:
        model = Sell
        fields = "__all__"


class SellItemSerializer(ModelSerializer):
    class Meta:
        model = SellItem
        fields = "__all__"

class CostSerializer(ModelSerializer):
    class Meta:
        model = Cost
        fields = "__all__"

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"