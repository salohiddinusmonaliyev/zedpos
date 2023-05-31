from django.shortcuts import render, redirect

from product.models import *
from clients.models import *
from sell.models import *
import datetime

# Create your views here.
def dashboard(request):
    sales = Sell.objects.all()
    kam = Product.objects.filter(quantity__lte=10)
    total_price = 0
    products = Product.objects.all()
    products_price = 0
    for p in products:
        products_price += products_price+p.price
    for s in sales:
        total_price+=s.total_price+total_price

    customers = Client.objects.all()
    debtors = Client.objects.filter(debt__gte=0)
    data = {
        "kam": kam,
        "sales": sales,
        "total_price": total_price,
        "products": products.count(),
        "products_price": products_price,
        "customers": customers.count(),
        "debtors": debtors.count(),
    }
    return render(request, "index.html", data)

# class Archive(APIView):
#     def get(self, request):
#         product = Product.objects.filter(is_active=False)
#         ser = ProductSerializer(product, many=True)
#         return Response(ser.data)