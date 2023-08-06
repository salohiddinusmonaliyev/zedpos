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


def product_edit(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        name = request.POST.get("name")
        code = int(request.POST.get("code"))
        price = request.POST.get("price")
        incoming = request.POST.get("incoming")
        quantity = request.POST.get("quantity")
        is_active = request.POST.get("is_active")
        measure = request.POST.get('measure')
        measure = Measure.objects.get(id=measure)
        if is_active == "on":
            is_active = True
        else:
            is_active = False

        try:
            if Product.objects.get(code=code).code == code and product.code != code:
                messages.error(request, "Code error. Bunday kodli mahsulot bor")
                return redirect(f"/product/{id}/edit/")

            else:
                product.code = code
                product.name = name
                product.arrival_price = incoming
                product.price = price
                product.quantity = quantity
                product.is_active = is_active
                product.measure = measure
                product.save()
                return redirect("/product/list/")
        except:
            product.code = code
            product.name = name
            product.arrival_price = incoming
            product.price = price
            product.quantity = quantity
            product.is_active = is_active
            product.measure = measure
            product.save()
            return redirect("/product/list/")
    else:
        product = Product.objects.get(id=id)
        measurements = Measure.objects.all()
        data = {
            "product": product,
            "measures": measurements
        }
        return render(request, "products/page-edit-product.html", data)


def product_add(request):
    name = request.POST.get("name")
    code = int(request.POST.get("code"))
    price = request.POST.get("price")
    incoming = request.POST.get("incoming")
    quantity = request.POST.get("quantity")
    measure = request.POST.get('measure')
    measure = Measure.objects.get(id=measure)
    try:
        if Product.objects.get(code=code).code == code:
            messages.error(request, "Code error. Bunday kodli mahsulot bor")
            return redirect("/product/add/")

        else:
            Product.objects.create(code=code,
                                   name=name,
                                   arrival_price=incoming,
                                   price=price,
                                   quantity=quantity,
                                   is_active=True,
                                   measure=measure)
            return redirect("/product/list/")
    except:
        Product.objects.create(name=name,
                               code=code,
                               arrival_price=incoming,
                               price=price,
                               quantity=quantity,
                               is_active=True,
                               measure=measure)
        return redirect("/product/list/")


def archive(request, a=None):
    if request.method == "POST":
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


def measurement_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Measure.objects.create(name=name)
        return redirect("/product/measurement/")
    else:
        return render(request, "products/add-measurement.html")


def measurements(request):
    data = {
        "measurements": Measure.objects.all(),
    }
    return render(request, "products/measurements.html", data)


def warehouse(request):
    data = {
        "items": AddProduct.objects.all()
    }
    return render(request, "products/warehouse.html", data)


def warehouse_add(request, a=None):
    if request.method == "POST":
        product = request.POST.get("product")
        product = Product.objects.get(id=product)
        dealer = request.POST.get("dealer")
        dealer = Dealer.objects.get(id=dealer)
        date = datetime.now()
        quantity = request.POST.get("quantity")
        total_price = request.POST.get("total_price")
        paid = request.POST.get("paid")
        price = request.POST.get("price")
        pq = product.quantity
        if int(total_price) != int(quantity) * int(product.price):
            messages.error(request, "Total price - error!")
            return redirect(f"/product/{a}/add/")
        else:
            if total_price == paid:
                status = "Paid"
            else:
                status = "Unpaid"
                dealer.debt = int(dealer.debt) + int(int(total_price) - int(paid))
            product.quantity = int(pq) + int(quantity)
            product.save()
            dealer.save()
            AddProduct.objects.create(product=product, dealer_id=dealer, date=date, quantity=quantity,
                                      total_price=total_price, price=price, status=status, paid=paid)
            return redirect('/product/list/')
    data = {
        "product": Product.objects.get(id=a),
        "dealers": Dealer.objects.all(),
    }
    return render(request, "products/add-warehouse.html", data)
