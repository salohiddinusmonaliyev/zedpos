from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializer import *


# Create your views here.
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientPayView(APIView):
    queryset = ClientPay.objects.all()
    serializer_class = ClientPaySerializer
    def get(self, request):
        snippets = ClientPay.objects.all()
        serializer = ClientPaySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientPaySerializer(data=request.data)
        if serializer.is_valid():
            if int(request.data.get("payment"))<=Client.objects.get(id=request.data.get("client")).debt:
                serializer.save()
                client = Client.objects.get(id=request.data.get("client"))
                client.debt = client.debt-serializer.data.get("payment")
                client.save()
            else:
                return Response({
                    "error": "Mijozning qarzi kiritgan summangizdan kam"
                })

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
