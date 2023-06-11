from django.shortcuts import render, redirect

from dealer.models import *
from warehouse.models import Warehouse


def list(request):
    data = {
        'dealers': Dealer.objects.all()
    }
    return render(request, 'dealers.html', data)

def add(request):
    if request.method=="POST":
        name = request.POST.get("name")
        pnum = str(request.POST.get("pnum"))
        Dealer.objects.create(name=name, phone_num=pnum)
        return redirect('/dealers/')
    return render(request, 'add-dealers.html')

def payment(request):
    payment = request.POST.get("payment")
    dealer = request.POST.get("dealer")
    dealer = Dealer.objects.get(id=dealer)
    Payment.objects.create(payment=payment, dealer=dealer)
    return redirect('/dealers/')

def dealer_brought(request, i):
    data = {
        "dealers": Warehouse.objects.filter(dealer_id=i)
    }
    return render(request, "dealers-brought.html", data)










# from rest_framework.viewsets import ModelViewSet
#
# from .models import *
# from . serializer import *
#
# # Create your views here.
# class DealerViewSet(ModelViewSet):
#     queryset = Dealer.objects.all()
#     serializer_class = DealerSerializer