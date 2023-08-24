from django.shortcuts import render, redirect

from dealer.models import *
from product.models import AddProduct


def list(request):
    data = {
        'dealers': Dealer.objects.filter(user=request.user)
    }
    return render(request, 'people/dealers.html', data)

def add(request):
    if request.method=="POST":
        name = request.POST.get("name")
        pnum = str(request.POST.get("pnum"))
        Dealer.objects.create(name=name, phone_num=pnum, user=request.user)
        return redirect('/dealers/')
    return render(request, 'people/add-dealers.html')

def payment(request):
    payment = request.POST.get("payment")
    dealer = request.POST.get("dealer")
    dealer = Dealer.objects.get(id=dealer)
    description = request.POST.get("description")
    Payment.objects.create(payment=payment, dealer=dealer, description=description, user=request.user)
    return redirect('/dealers/')

# def dealer_brought(request, i):
#     data = {
#         "dealers": AddProduct.objects.filter(dealer_id=i)
#     }
#     return render(request, "people/dealers-brought.html", data)










# from rest_framework.viewsets import ModelViewSet
#
# from .models import *
# from . serializer import *
#
# # Create your views here.
# class DealerViewSet(ModelViewSet):
#     queryset = Dealer.objects.all()
#     serializer_class = DealerSerializer