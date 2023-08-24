from django.shortcuts import render, redirect
from .models import *

def clients_list(request):
    data = {
        "customers": Client.objects.filter(user=request.user),
    }
    return render(request, 'people/page-list-customers.html', data)

def customer_delete(request, i):
    Client.objects.get(id=i, user=request.user).delete()
    return redirect("/customers/")

def debt_payment(request):
    payment = request.POST.get('payment')
    customer = request.POST.get('customer')
    comment = request.POST.get("comment")
    customer_debt = Client.objects.get(id=customer, user=request.user)
    customer_debt2 = Client.objects.get(id=customer, user=request.user).debt

    customer_debt.debt = int(customer_debt2)-int(payment)
    customer_debt.save()
    CustomerPayment.objects.create(customer=customer_debt, paymnet=payment, comment=comment, user=request.user)
    return redirect('/customers/')


def customer_add(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        debt = request.POST.get('debt')
        p_num = request.POST.get('p_num')
        Client.objects.create(first_name=first_name, last_name=last_name, p_num=p_num, debt=debt, count=0, sale=0)
        return redirect('/customers/')
    return render(request, "people/page-add-customers.html")

def customer_history(request, i):
    data = {
        "customers": CustomerPayment.objects.filter(customer_id=i)
    }
    return render(request, "people/customer-history.html", data)
















# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from rest_framework.viewsets import ModelViewSet
#
# from .models import *
# from .serializer import *
#
#
# # Create your views here.
# class ClientViewSet(ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#
# class ClientPayView(APIView):
#     queryset = ClientPay.objects.all()
#     serializer_class = ClientPaySerializer
#     def get(self, request):
#         snippets = ClientPay.objects.all()
#         serializer = ClientPaySerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ClientPaySerializer(data=request.data)
#         if serializer.is_valid():
#             if int(request.data.get("payment"))<=Client.objects.get(id=request.data.get("client")).debt:
#                 serializer.save()
#                 client = Client.objects.get(id=request.data.get("client"))
#                 client.debt = client.debt-serializer.data.get("payment")
#                 client.save()
#             else:
#                 return Response({
#                     "error": "Mijozning qarzi kiritgan summangizdan kam"
#                 })
#
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
