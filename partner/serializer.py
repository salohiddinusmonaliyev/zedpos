from rest_framework.serializers import ModelSerializer

from .models import *

class DealerSerializer(ModelSerializer):
    class Meta:
        model = Dealer
        fields = "__all__"

class DealerOutputSerializer(ModelSerializer):
    class Meta:
        model = DealerOutput
        fields = "__all__"
