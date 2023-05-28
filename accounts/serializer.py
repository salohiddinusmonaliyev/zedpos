from rest_framework.serializers import ModelSerializer

from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
