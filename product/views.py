from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *

@login_required(login_url='/accounts/login/')
def product_list(request):

    data = {
        'products': Product.objects.filter(is_active=True, user=request.user).order_by('code'),
    }
    return render(request, 'products/page-list-product.html', data)

@login_required(login_url='/accounts/login/')
def product_add_page(request):

    data = {
        "measures": Measure.objects.filter(user=request.user)
    }
    return render(request, 'products/page-add-product.html', data)

@login_required(login_url='/accounts/login/')
def product_edit(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id, user=request.user)
        name = request.POST.get("name")
        code = int(request.POST.get("code"))
        price = request.POST.get("price")
        incoming = request.POST.get("incoming")
        quantity = request.POST.get("quantity")
        is_active = request.POST.get("is_active")
        measure = request.POST.get('measure')
        measure = Measure.objects.get(id=measure, user=request.user)
        if is_active == "on":
            is_active = True
        else:
            is_active = False

        try:
            if Product.objects.get(code=code, user=request.user).code == code and product.code != code:
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
        product = Product.objects.get(id=id, user=request.user)
        measurements = Measure.objects.filter(user=request.user)
        data = {
            "product": product,
            "measures": measurements
        }
        return render(request, "products/page-edit-product.html", data)


@login_required(login_url='/accounts/login/')
def product_add(request):
    name = request.POST.get("name")
    code = int(request.POST.get("code"))
    price = request.POST.get("price")
    incoming = request.POST.get("incoming")
    quantity = request.POST.get("quantity")
    measure = request.POST.get('measure')
    measure = Measure.objects.get(id=measure, user=request.user)
    try:
        if Product.objects.get(code=code, user=request.user).code == code:
            messages.error(request, "Code error. Bunday kodli mahsulot bor")
            return redirect("/product/add/")

        else:
            Product.objects.create(code=code,
                                   name=name,
                                   arrival_price=incoming,
                                   price=price,
                                   quantity=quantity,
                                   is_active=True,
                                   measure=measure, user=request.user)
            return redirect("/product/list/")
    except:
        Product.objects.create(name=name,
                               code=code,
                               arrival_price=incoming,
                               price=price,
                               quantity=quantity,
                               is_active=True,
                               measure=measure, user=request.user)
        return redirect("/product/list/")


@login_required(login_url='/accounts/login/')
def archive(request, a=None):
    if request.method == "POST":
        product = Product.objects.get(id=a, user=request.user)
        product.is_active = False
        product.save()
        return redirect('/product/list/')
    data = {
        "products": Product.objects.filter(is_active=False, user=request.user)
    }
    return render(request, "products/page-list-archive-product.html", data)


@login_required(login_url='/accounts/login/')
def archive_delete(request, a):

    product = Product.objects.get(id=a, user=request.user)
    product.is_active = True
    product.save()
    return redirect("/product/list/")

@login_required(login_url='/accounts/login/')
def measurement_add(request):

    if request.method == "POST":
        name = request.POST.get('name')
        Measure.objects.create(name=name, user=request.user)
        return redirect("/product/measurement/")
    else:
        return render(request, "products/add-measurement.html")

@login_required(login_url='/accounts/login/')
def measurements(request):
    data = {
        "measurements": Measure.objects.filter(user=request.user),
    }
    return render(request, "products/measurements.html", data)

@login_required(login_url='/accounts/login/')
def warehouse(request):

    data = {
        "items": AddProduct.objects.filter(user=request.user)
    }
    return render(request, "products/warehouse.html", data)

@login_required(login_url='/accounts/login/')
def warehouse_add(request, a=None):

    if request.method == "POST":
        product = request.POST.get("product")
        product = Product.objects.get(id=product, user=request.user)
        date = datetime.now()
        quantity = request.POST.get("quantity")
        pq = product.quantity
        product.quantity = int(pq) + int(quantity)
        product.save()
        total_price = int(quantity) * int(product.price)
        AddProduct.objects.create(product=product, date=date, quantity=quantity,
                                      total_price=total_price, user=request.user)
        return redirect('/product/list/')
    data = {
        "product": Product.objects.get(id=a, user=request.user),
        "dealers": Dealer.objects.filter(user=request.user),
    }
    return render(request, "products/add-warehouse.html", data)

@login_required(login_url='/accounts/login/')
def product_item(request, pk):

    data = {
        "items": AddProduct.objects.filter(product_id=pk, user=request.user)
    }
    return render(request, "people/dealers-brought.html", data)


@login_required(login_url='/accounts/login/')
def unarchive(request, pk):

    product = Product.objects.get(id=pk, user=request.user)
    product.is_active = True
    product.save()
    return redirect('/product/list/')
