from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *


def product_list(request):
    data = {
        'products': Product.objects.filter(is_active=True).order_by('code'),
    }
    return render(request, 'products/page-list-product.html', data)

def product_add_page(request):
    data = {
        "measures": Measure.objects.all()
    }
    return render(request, 'products/page-add-product.html', data)

def product_add(request):
    name = request.POST.get("name")
    code = int(request.POST.get("code"))
    price = request.POST.get("price")   
    incoming = request.POST.get("incoming")
    quantity = request.POST.get("quantity")
    is_active = request.POST.get("is_active")
    measure = request.POST.get('measure')
    measure = Measure.objects.get(id=measure)
    if is_active=="on":
        is_active=True
    else:
        is_active=False
    # print("-------------------/-")
    # print(Product.objects.get(code=int(code)))
    try:
        if Product.objects.get(code=code).code == code:
            messages.error(request, "Code error. Bunday kodli mahsulot bor")
            return redirect("/product/add/")

        else:
            Product.objects.create(code=code, name=name, arrival_price=incoming, price=price, quantity=quantity, is_active=is_active, measure=measure)
            return redirect("/product/list/")
    except:
        Product.objects.create(code=code, name=name, arrival_price=incoming, price=price, quantity=quantity,
                               is_active=is_active, measure=measure)
        return redirect("/product/list/")

def archive(request, a=None):
    if request.method=="POST":
        product = Product.objects.get(id=a)
        product.is_active = False
        product.save()
        return redirect('/product/list/')
    data = {
        "products": Product.objects.filter(is_active=False)
    }
    return render(request, "products/page-list-archive-product.html", data)

def archive_delete(request, a):
    product = Product.objects.get(id=a)
    product.is_active = True
    product.save()
    return redirect("/product/list/")


def measure(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Measure.objects.create(name=name)
    return redirect("/product/list/")