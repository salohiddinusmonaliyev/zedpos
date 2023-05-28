from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import *
from clients.models import *
from product.serializer import ProductSerializer
from sell.models import *
import datetime

# Create your views here.
class MainView(APIView):
    def get(self, request,a=None, b=None):
        if a==None and b==None:
            a=str(datetime.date.today())
            b=str(datetime.date.today())

        # Umumiy sonlar
        products = Product.objects.filter(is_active=True).count()
        clients = Client.objects.all().count()
        qarzdorlar = Client.objects.filter(debt__lte=0).count()

        # sotuv
        sotuv = []

        # daromad
        d = Sell.objects.all()
        daromad = 0
        for u in d:
            if str(u.time.date())>=a and str(u.time.date())<=b:
                daromad = int(daromad)+int(u.total_price)
                sotuv.append(u)
        sotuv = len(sotuv)


        # harajat
        h = Cost.objects.all()
        harajat = 0
        for ha in h:
            if str(ha.date.date()) >= a and str(ha.date.date()) <= b:
                harajat = harajat + ha.money

        # top 5 mahsulotlar
        sellitems = SellItem.objects.all()

        # tashqi haqlarsli
        qarzlar = Client.objects.all()
        debt = 0
        for q in qarzlar:
            debt=debt+q.debt

        # do'kondagi tovarlar
        t = Product.objects.all()
        tovarlar = 0
        for y in t:
            tovarlar = tovarlar + y.incoming_price

        # foyda
        data = SellItem.objects.filter()
        foyda = 0
        for i in data:
            print("------------------------")
            print(i.date)
            if str(i.date.date()) >= a and str(i.date.date()) <= b:

                product_price = (int(i.quantity)*i.product_id.price) - (int(i.quantity)*int(i.discount))
                product_kelgan = (int(i.quantity)*i.product_id.incoming_price)
                foyda = foyda + (product_price-product_kelgan)
        foyda = foyda - harajat

        # 10 tadan kam qolgan
        product = Product.objects.filter(is_active=True, quantity__lte=10)
        return Response({
            "sotuvlar":sotuv,
            "daromad":daromad,
            "foyda":foyda,
            "xarajat":harajat,
            "tovarlar_soni":products,
            "mijozlar":clients,
            "qarzdorlar":qarzdorlar,
            "10_kam_qolgan":product,
            "tashqi_haqlar":debt,
            "tovarlar_summasi":tovarlar,
        })


class NewProduct(APIView):
    def get(self, request, p, q):
        quantity = int(Product.objects.get(id=p).quantity)+q
        product = Product.objects.get(id=p)
        product.quantity = quantity
        product.save()
        return Response("qo'shildi")


class Archive(APIView):
    def get(self, request):
        product = Product.objects.filter(is_active=False)
        ser = ProductSerializer(product, many=True)
        return Response(ser.data)