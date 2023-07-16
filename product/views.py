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
    is_active = request.POST.get("is_active")
    measure = request.POST.get('measure')
    measure = Measure.objects.get(id=measure)
    if is_active == "on":
        is_active = True
    else:
        is_active = False
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
                                   is_active=is_active,
                                   measure=measure)
            return redirect("/product/list/")
    except:
        Product.objects.create(name=name,
                               code=code,
                               arrival_price=incoming,
                               price=price,
                               quantity=quantity,
                               is_active=is_active,
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
