from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializer import *

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
