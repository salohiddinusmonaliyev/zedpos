from django.shortcuts import render, redirect

from dealer.models import Payment
from product.models import *
from clients.models import *
from sell.models import *
import datetime

# Create your views here.
def dashboard(request):
    sales = Sell.objects.all()
    kam = Product.objects.filter(is_active=True, quantity__lte=10)
    total_price = 0
    products = Product.objects.filter(is_active=True)
    products_price = 0
    data = SellItem.objects.filter()
    foyda = 0
    for i in data:
        product_price = (int(i.quantity) * i.product.price)
        product_kelgan = (int(i.quantity) * i.product.incoming_price)
        foyda = foyda + (product_price - product_kelgan)
    my_list = []
    for p in products:
        products_price = products_price+(p.incoming_price*p.quantity)
        my_list.append(p.count)
    for s in sales:
        if s.total_price==None:
            total_price+=0
        else:
            total_price=int(s.total_price)+int(total_price)
    dealers = Payment.objects.all()
    pay = 0
    for p in dealers:
        pay += p.payment

    customers = Client.objects.all()
    debtors = Client.objects.filter(debt__gte=1)

    costs = Cost.objects.all()
    cost = 0
    for c in costs:
        cost+=c.cost

    data = {
        "kam": kam,
        "sales": sales,
        "total_price": total_price-pay,
        "products": products.count(),
        "products_price": products_price,
        "customers": customers.count(),
        "debtors": debtors.count(),
        "cost": cost,
        "foyda": foyda,
        "top5": Product.objects.all().order_by('count')[:5],
    }
    return render(request, "index.html", data)

# class Archive(APIView):
#     def get(self, request):
#         product = Product.objects.filter(is_active=False)
#         ser = ProductSerializer(product, many=True)
#         return Response(ser.data)