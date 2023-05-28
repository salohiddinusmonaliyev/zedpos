from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import generics, status

from .serializer import *
from .models import *

# Create your views here.
class SellViewSet(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class SellItemViewSet(APIView):
    queryset = SellItem.objects.all()
    serializer_class = SellItemSerializer
    def get(self, request):
        snippets = SellItem.objects.all()
        serializer = SellItemSerializer(snippets, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SellItemSerializer(data=request.data)
        if serializer.is_valid():
            # print(request.data.get("quantity"))
            # print("------------------------")
            # print(int(request.data.get("product")))
            product_quantity = Product.objects.get(id=int(request.data.get("product")))
            if product_quantity.quantity < int(request.data.get("quantity")):
                return Response({
                    "error":"Do'konda bu mahsulotdan kam"
                }, status=status.HTTP_400_BAD_REQUEST)
            elif product_quantity.quantity >= int(request.data.get("quantity")):
                product = Product.objects.get(id=product_quantity.id)
                product.quantity = product.quantity-int(request.data.get("quantity"))
                product.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CostViewSet(ModelViewSet):

    queryset = Cost.objects.all()
    serializer_class = CostSerializer


class PaymentView(APIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    def get(self, request):
        snippets = Payment.objects.all()
        serializer = PaymentSerializer(snippets, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            # print(request.data.get("client"))
            if Sell.objects.get(id=request.data.get("sell_id")).total_price == request.data.get("payment"):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            elif Sell.objects.get(id=request.data.get("sell_id")).total_price != request.data.get("payment") and request.data.get("client")=="":
                return Response({
                    "error": "To'lov to'liq to'lanmadi. Mijozni kiriting"
                })
            elif Sell.objects.get(id=request.data.get("sell_id")).total_price != request.data.get("payment") and request.data.get("client")!="":
                totel_price = Sell.onjects.get(id=request.data.get("sell_id").id).total_price
                payment = request.data.get("payment")
                debt = totel_price-payment
                client_id = request.data.get("client").id
                client=Client.objects.get(id=client_id)
                client.debt = debt
                client.save()
                return Response({
                    "message": "Pul to'liq to'lanmadi. Qoldiq mijozga qarz sifatida yozildi"
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Hisoblash(APIView):
    def get(self, request, a):
        try:
            s = Sell.objects.get(id=a)
            data = SellItem.objects.filter(sell_id=s)
            products = ""
            summa = 0
            for i in data:
                product_price = i.product_id.price
                total_price = (product_price*i.quantity)+summa
                foyda = (int(i.product_id.incoming_price) * int(i.quantity))
                foyda = total_price - foyda
                discount = 0
                products = products+f"{i.quantity} {i.product_id.measure} {i.product_id.name}"+", "
                summa = total_price
                if i.discount!=0:
                    discount = int(i.quantity)*int(discount+i.discount)
                else:
                    discount = 0
            s.total_price = total_price

            s.save()
            return Response({
                "Olingan_mahsulotlar": products,
                "Umumiy_hisob": total_price,
                "So'ngi hisob": summa - discount,
                "Chegirmasiz_foyda": foyda,
                "Chegirmali_foyda": foyda - discount,
            }, status=status.HTTP_200_OK)
        except UnboundLocalError:
            return Response({
                "error":"Xatolik bor. Bu savat bo'sh bo'lishi mumkin"
            })

