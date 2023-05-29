from django.shortcuts import render, redirect

from product.models import *
from clients.models import *
from sell.models import *
import datetime

# Create your views here.
def dashboard(request):
    sales = Sell.objects.all()
    kam = Product.objects.filter(quantity__lte=10)
    data = {
        "kam": kam,
    }
    return render(request, "index.html", data)

# class Archive(APIView):
#     def get(self, request):
#         product = Product.objects.filter(is_active=False)
#         ser = ProductSerializer(product, many=True)
#         return Response(ser.data)