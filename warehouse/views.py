from datetime import datetime

from django.shortcuts import render, redirect

from dealer.models import Dealer
from product.models import Product
from warehouse.models import Warehouse


# Create your views here.


def warehouse(request):
    data = {
        "items": Warehouse.objects.all()
    }
    return render(request, "warehouse.html", data)

def warehouse_add(request):
    if request.method=="POST":
        product = request.POST.get("product")
        product_price = Product.objects.get(id=product).arrival_price
        product = Product.objects.get(id=product)
        dealer = request.POST.get("dealer")
        dealer = Dealer.objects.get(id=dealer)
        date = datetime.now()
        quantity = request.POST.get("quantity")
        total_price = request.POST.get("total_price")
        aprice = request.POST.get("aprice")
        status = request.POST.get("status")
        price = request.POST.get("price")

        if aprice == product_price:
            pq = product.quantity
            product.quantity = int(pq) + int(quantity)
            product.save()
        elif aprice!=product_price:
            print("------------")
            print(False)
            product.is_active = False
            product.save()
            code = product.code
            name = product.name
            coming = aprice
            quantity = float(quantity) + float(product.quantity)

            Product.objects.create(code=code, name=name, arrival_price=coming, price=price, quantity=quantity, is_active=True)
        Warehouse.objects.create(product=product, dealer_id=dealer, date=date, quantity=quantity, total_price=total_price, price=price, status=status)
        return redirect('/warehouse/list/')
    data = {
        "products": Product.objects.filter(is_active=True).order_by('code'),
        "dealers": Dealer.objects.all(),
    }
    return render(request, "add-warehouse.html", data)