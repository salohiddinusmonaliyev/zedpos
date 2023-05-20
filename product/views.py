from django.shortcuts import render

from .models import *


def product_list(request):
    data = {
        'products': Product.objects.all(),
    }
    return render(request, 'page-list-product.html', data)
