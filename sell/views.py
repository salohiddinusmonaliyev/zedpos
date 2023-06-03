from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View

from .models import *

from django.contrib import messages



def sale_list(request):
    data = {
        "sales": Sell.objects.all().order_by('id'),
    }
    return render(request, "page-list-sale.html", data)

def sale_add(request, s):
    saleitem = SellItem.objects.filter(sell_id=s)
    total_price = 0
    for sale in saleitem:
        total_price = total_price + (sale.product.price*sale.quantity)
    data = {
        "products": Product.objects.filter(is_active=True).order_by('code'),
        "clients": Client.objects.all(),
        "sale": s,
        "saleitems": saleitem,
        "checkout": Sell.objects.get(id=s).checkout,
        "total_price": total_price,

    }
    return render(request, "page-add-sale.html", data)


def create_sale(request):
    saleid = Sell.objects.create(time=datetime.now())
    saleid = saleid.id
    return redirect(f'/sale-add/{saleid}/')

def saleitem_delete(request, id, saleid):
    saleitem = SellItem.objects.get(id=id)
    product = Product.objects.get(id=saleitem.product.id)
    product.quantity = product.quantity + saleitem.quantity
    product.save()
    SellItem.objects.get(id=id).delete()
    return redirect(f"/sale-add/{saleid}")

def saleitem_create(request, saleid):
    if request.method=="POST":
        try:
            sale = Sell.objects.get(id=saleid)
            saleitems = SellItem.objects.all()
            code = request.POST.get("code")
            quantity = request.POST.get("quantity")
            product = Product.objects.get(is_active=True, code=code)
            # print("-----------")
            # print(product.quantity-int(quantity))
            for s in saleitems:
                if s.product==product and s.sell_id==sale:
                    return redirect(f"/sale-add/{saleid}/")
            if product.quantity-int(quantity)>=0:
                product.quantity = product.quantity-int(quantity)
                product.count += int(quantity)
                product.save()
                SellItem.objects.create(sell_id=sale, product=product, date=datetime.now(), quantity=quantity)

            return redirect(f"/sale-add/{saleid}/")
        except:
            message = messages.error(request, "Code error")
            return redirect(f"/sale-add/{saleid}/")

def checkout(request, saleid):
    if request.method=="POST":
        saleitem = SellItem.objects.filter(sell_id=saleid)
        total_price = 0
        for sale in saleitem:
            total_price = total_price + (sale.product.price * sale.quantity)
        sale = Sell.objects.get(id=saleid)
        paid = request.POST.get('paid')
        if paid==total_price:
            sale.checkout = True
            sale.total_price = total_price
            customer = request.POST.get('customer')
            sale.paid = paid
            if customer=="---------":
                sale.client = None
            else:
                customer = Client.objects.get(id=customer)
                sale.client = customer
            sale.save()
        else:
            sale.checkout = True
            sale.total_price = total_price
            customer = request.POST.get('customer')
            if customer=="---------":
                messages.error(request, "error")
            else:
                customer = Client.objects.get(id=customer)
                customer.debt += int(total_price)-int(paid)
                customer.save()
                sale.client = customer
            sale.paid = paid
            sale.save()
        return redirect(f"/sale-list/")

def sale_delete(request, saleid):
    sale = Sell.objects.get(id=saleid)
    saleitems = SellItem.objects.filter(sell_id=sale)
    for saleitem in saleitems:
        saleitem.delete()
    sale.delete()
    return redirect("/sale-list/")

def refresh(request, saleid, tp):
    sale = Sell.objects.get(id=saleid)
    sale.total_price = tp
    sale.save()
    return redirect('/sale-list/')

def cost_list(request):
    data = {
        "costs": Cost.objects.all()
    }
    return render(request, "list-cost.html", data)

# def cost_category(request):
#     data = {
#         "categories": CostCategory.objects.all()
#     }
#     return render(request, "list-category.html", data)

def cost_create(request):
    if request.method=="POST":
        cost = request.POST.get("cost")
        worker = request.POST.get("worker")
        category = request.POST.get("category")
        category = CostCategory.objects.get(id=category)
        worker = User.objects.get(id=worker)
        Cost.objects.create(cost=cost, category=category, worker=worker, date=datetime.now())
        return redirect('/cost-list/')
    data = {
        "category": CostCategory.objects.all(),
        "worker": User.objects.all()
    }
    return render(request, "add-cost.html", data)



#
# class SellItemViewSet(APIView):
#     queryset = SellItem.objects.all()
#     serializer_class = SellItemSerializer
#     def get(self, request):
#         snippets = SellItem.objects.all()
#         serializer = SellItemSerializer(snippets, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = SellItemSerializer(data=request.data)
#         if serializer.is_valid():
#             # print(request.data.get("quantity"))
#             # print("------------------------")
#             # print(int(request.data.get("product")))
#             product_quantity = Product.objects.get(id=int(request.data.get("product")))
#             if product_quantity.quantity < int(request.data.get("quantity")):
#                 return Response({
#                     "error":"Do'konda bu mahsulotdan kam"
#                 }, status=status.HTTP_400_BAD_REQUEST)
#             elif product_quantity.quantity >= int(request.data.get("quantity")):
#                 product = Product.objects.get(id=product_quantity.id)
#                 product.quantity = product.quantity-int(request.data.get("quantity"))
#                 product.save()
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CostViewSet(ModelViewSet):
#
#     queryset = Cost.objects.all()
#     serializer_class = CostSerializer
#
#
# class PaymentView(APIView):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer
#     def get(self, request):
#         snippets = Payment.objects.all()
#         serializer = PaymentSerializer(snippets, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = PaymentSerializer(data=request.data)
#         if serializer.is_valid():
#             # print(request.data.get("client"))
#             if Sell.objects.get(id=request.data.get("sell_id")).total_price == request.data.get("payment"):
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             elif Sell.objects.get(id=request.data.get("sell_id")).total_price != request.data.get("payment") and request.data.get("client")=="":
#                 return Response({
#                     "error": "To'lov to'liq to'lanmadi. Mijozni kiriting"
#                 })
#             elif Sell.objects.get(id=request.data.get("sell_id")).total_price != request.data.get("payment") and request.data.get("client")!="":
#                 totel_price = Sell.onjects.get(id=request.data.get("sell_id").id).total_price
#                 payment = request.data.get("payment")
#                 debt = totel_price-payment
#                 client_id = request.data.get("client").id
#                 client=Client.objects.get(id=client_id)
#                 client.debt = debt
#                 client.save()
#                 return Response({
#                     "message": "Pul to'liq to'lanmadi. Qoldiq mijozga qarz sifatida yozildi"
#                 })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class Hisoblash(APIView):
#     def get(self, request, a):
#         try:
#             s = Sell.objects.get(id=a)
#             data = SellItem.objects.filter(sell_id=s)
#             products = ""
#             summa = 0
#             for i in data:
#                 product_price = i.product_id.price
#                 total_price = (product_price*i.quantity)+summa
#                 foyda = (int(i.product_id.incoming_price) * int(i.quantity))
#                 foyda = total_price - foyda
#                 discount = 0
#                 products = products+f"{i.quantity} {i.product_id.measure} {i.product_id.name}"+", "
#                 summa = total_price
#                 if i.discount!=0:
#                     discount = int(i.quantity)*int(discount+i.discount)
#                 else:
#                     discount = 0
#             s.total_price = total_price
#
#             s.save()
#             return Response({
#                 "Olingan_mahsulotlar": products,
#                 "Umumiy_hisob": total_price,
#                 "So'ngi hisob": summa - discount,
#                 "Chegirmasiz_foyda": foyda,
#                 "Chegirmali_foyda": foyda - discount,
#             }, status=status.HTTP_200_OK)
#         except UnboundLocalError:
#             return Response({
#                 "error":"Xatolik bor. Bu savat bo'sh bo'lishi mumkin"
#             })
#
