from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View

from .models import *

from django.contrib import messages



def sale_list(request):
    for sell in Sell.objects.all().order_by('id'):
        SellItem.objects.filter(sell_id_id=sell.id)
    data = {
        "sales": Sell.objects.all().order_by('id'),
    }
    return render(request, "sale/page-list-sale.html", data)

def sale_add(request, s):
    saleitem = SellItem.objects.filter(sell_id=s)
    sale_item = []
    for item in saleitem:
        sale_item.append({item.id: item.quantity*(item.product.price-item.discount)})
    print(sale_item)
    total_price = 0
    for sale in saleitem:
        total_price = int((total_price + (sale.product.price*sale.quantity))-(sale.discount*sale.quantity))
    data = {
        "products": Product.objects.filter(is_active=True).order_by('code'),
        "clients": Client.objects.all(),
        "sale": s,
        "saleitems": saleitem,
        "checkout": Sell.objects.get(id=s).checkout,
        "total_price": total_price,
        "sale_item": sale_item,

    }
    return render(request, "sale/page-add-sale.html", data)


def sale_create(request):
    saleid = Sell.objects.create(time=datetime.now())
    saleid = saleid.id
    return redirect(f'/sale/add/{saleid}/')

def saleitem_delete(request, id, saleid):
    saleitem = SellItem.objects.get(id=id)
    product = Product.objects.get(id=saleitem.product.id)
    product.quantity = product.quantity + saleitem.quantity
    product.save()
    SellItem.objects.get(id=id).delete()
    return redirect(f"/sale/add/{saleid}")

def saleitem_create(request, saleid):
    if request.method=="POST":
        try:
            sale = Sell.objects.get(id=saleid)
            saleitems = SellItem.objects.all()
            code = request.POST.get("code")
            quantity = request.POST.get("quantity")
            discount = request.POST.get("discount")
            product = Product.objects.get(is_active=True, code=code)
            # print("-----------")
            # print(product.quantity-int(quantity))
            # for s in saleitems:
            #     if s.product==product and s.sell_id==sale:
            #         return redirect(f"/sale/add/{saleid}/")
            if product.quantity-int(quantity)>=0:
                product.quantity = product.quantity-int(quantity)
                product.count += int(quantity)
                product.save()
                SellItem.objects.create(sell_id=sale, product=product, date=datetime.now(), quantity=quantity, discount=discount)

            return redirect(f"/sale/add/{saleid}/")
        except:
            message = messages.error(request, "Code error")
            return redirect(f"/sale/add/{saleid}/")

def checkout(request, saleid):
    if request.method=="POST":
        saleitem = SellItem.objects.filter(sell_id=saleid)
        total_price = 0
        for sale in saleitem:
            total_price = (total_price + (sale.product.price * sale.quantity))-(sale.discount*sale.quantity)
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
                customer.debt = int(total_price)-float(paid)
                customer.save()
                sale.client = customer
            sale.paid = paid
            sale.save()
        return redirect(f"/sale/list/")

def sale_delete(request, saleid):
    sale = Sell.objects.get(id=saleid)
    saleitems = SellItem.objects.filter(sell_id=sale)
    for saleitem in saleitems:
        saleitem.delete()
    sale.delete()
    return redirect("/sale/list/")

def refresh(request, saleid, tp):
    sale = Sell.objects.get(id=saleid)
    sale.total_price = tp
    sale.save()
    return redirect('/sale/list/')

def cost_list(request):
    data = {
        "costs": Cost.objects.all()
    }
    return render(request, "sale/list-cost.html", data)

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
    return render(request, "sale/add-cost.html", data)

def saleitem_list(request, s):
    saleitem = SellItem.objects.filter(sell_id=s)
    sale_item = []
    for item in saleitem:
        sale_item.append({item.id: item.quantity*(item.product.price-item.discount)})
    print(sale_item)
    total_price = 0
    for sale in saleitem:
        total_price = int((total_price + (sale.product.price*sale.quantity))-(sale.discount*sale.quantity))
    data = {
        "products": Product.objects.filter(is_active=True).order_by('code'),
        "clients": Client.objects.all(),
        "sale": s,
        "saleitems": saleitem,
        "checkout": Sell.objects.get(id=s).checkout,
        "total_price": total_price,
        "sale_item": sale_item,

    }
    return render(request, "sale/saleitem_list.html", data)

def return_create(request, sale, saleitem):
    if request.method=="POST":
        customer = request.POST.get("customer")
        customer = Client.objects.get(id=customer)
        quantity = request.POST.get("quantity")
        worker = request.POST.get("worker")
        item = SellItem.objects.get(id=saleitem)
        saleitem2 = SellItem.objects.filter(sell_id_id=sale)
        total_price = 0
        sell = Sell.objects.get(id=sale)
        for sale2 in saleitem2:
            total_price = (total_price + (sale2.product.price * sale2.quantity)) - (sale2.discount * sale2.quantity)
        if sell.paid == sell.total_price:
            paid = item.product.price * int(quantity) - (item.discount * int(quantity))
            sell.total_price = total_price-paid
            sell.paid = total_price-paid
            item.quantity = item.quantity - int(quantity)
            item.save()
            sell.save()
            Return.objects.create(sellitem_id=saleitem, customer=customer, paid=paid, quantity=quantity,
                                  worker_id=worker)
        elif customer.debt>0:
            messages.error(request, "Mijoz avval qarzini to'liq to'lasin")
            return redirect("/customers/")

        return redirect("/sale/return/")
    # saleitem = SellItem.objects.get(id=saleitem)
    # sale = Sell.objects.get()
    data = {
        "sale": sale,
        "saleitem": saleitem,
        "customers": Client.objects.all(),
        "staff": Worker.objects.all(),
    }
    return render(request, "sale/add-returns.html", data)

def return_list(request):
    data = {
        "items": Return.objects.all()
    }
    return render(request, "sale/list-returns.html", data)

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
