from rest_framework.serializers import ModelSerializer

from sell.models import ClientPay
from .models import *

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class ClientPaySerializer(ModelSerializer):
    class Meta:
        model = ClientPay
        fields = "__all__"
