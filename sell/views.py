import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import *

from django.contrib import messages
# payments/views.py

from datetime import datetime

from django.shortcuts import render
import pdfkit
from django.http import HttpResponse

@login_required(login_url='/accounts/login/')
def generate_cheque_pdf(request, pk):
    # Data to be passed to the Jinja2 template
    items = SellItem.objects.filter(sell_id_id=pk, user=request.user)
    total_price = 0
    for item in items:
        total_price += (int(item.price)-int(item.discount))*float(item.quantity)
    cheque_data = {
        "cheque": Sell.objects.get(id=pk, user=request.user),
        "items": items,
        "products": Product.objects.filter(user=request.user).order_by('code'),
        "clients": Client.objects.filter(user=request.user),
        "item_total_price": total_price,
    }

    # Render the cheque template using Jinja2
    template_name = 'cheque.html'
    rendered_template = render(request, template_name, cheque_data)

    # Generate PDF using pdfkit
    rendered_content = rendered_template.content.decode('utf-8')

    # Generate PDF using pdfkit and provide the path to wkhtmltopdf executable
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdf = pdfkit.from_string(rendered_content, False, configuration=config)

    # Set the Content-Disposition header to open the PDF in a new tab
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="cheque.pdf"'

    return response




@login_required(login_url='/accounts/login/')
def sale_list(request):
    if request.user.status == "Paid":
        for sell in Sell.objects.all().order_by('id'):
            SellItem.objects.filter(sell_id_id=sell.id)
        data = {
            "sales": Sell.objects.filter(user=request.user).order_by('id'),
        }
        return render(request, "sale/page-list-sale.html", data)
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")


def sale_add(request, s):
    if request.user.status == "Paid":
        saleitem = SellItem.objects.filter(sell_id=s, user=request.user)
        sale_item = []
        for item in saleitem:
            sale_item.append({item.id: item.quantity*(item.price-item.discount)})
        total_price = 0
        discount = 0
        for sale in saleitem:
            total_price = int((total_price + (sale.price*sale.quantity))-(sale.discount*sale.quantity))
            discount += (sale.discount*sale.quantity)


        data = {
            "products": Product.objects.filter(is_active=True, user=request.user).order_by('code'),
            "clients": Client.objects.filter(user=request.user),
            "sale": s,
            "saleitems": saleitem,
            "checkout": Sell.objects.get(id=s, user=request.user).checkout,
            "total_price": total_price,
            "sale_item": sale_item,
            "discount": discount,
            "total_price2": total_price+discount

        }
        return render(request, "sale/page-add-sale.html", data)
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def sale_create(request):
    if request.user.status == "Paid":
        saleid = Sell.objects.create(time=datetime.now(), user=request.user)
        saleid = saleid.id
        return redirect(f'/sale/add/{saleid}/')
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def saleitem_delete(request, id, saleid):
    if request.user.status == "Paid":
        SellItem.objects.get(id=id, user=request.user).delete()
        return redirect(f"/sale/add/{saleid}")
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

# def saleitem_create(request, saleid):
#     try:
#         if request.method=="POST":
#             sale = Sell.objects.get(id=saleid)
#             saleitems = SellItem.objects.all()
#             code = request.POST.get("code")
#             quantity = request.POST.get("quantity")
#             discount = request.POST.get("discount")
#             if discount is None or not discount:
#                 discount = 0
#
#             product = Product.objects.get(is_active=True, code=code)
#             for s in saleitems:
#                 if s.product == product and s.sell_id == sale:
#                     message = messages.error(request, "Bu mahsulot savatda bor")
#                     return redirect(f"/sale/add/{saleid}/")
#             SellItem.objects.create(sell_id=sale, product=product, price=product.price, date=datetime.now(), quantity=quantity, discount=discount)
#
#             return redirect(f"/sale/add/{saleid}/")
#

def calculate_sellitem_total_price(price, quantity, discount):
    return (price-discount) * quantity

@login_required(login_url='/accounts/login/')
def saleitem_create(request, saleid):
    if request.user.status == "Paid":
        try:
            if request.method == "POST":
                sale = Sell.objects.get(id=saleid, user=request.user)
                saleitems = SellItem.objects.filter(user=request.user)
                code = request.POST.get("code")
                # quantity = request.POST.get("quantity")
                discount = int(request.POST.get("discount"))

                if discount is None or not discount:
                    discount = 0
                product = Product.objects.get(is_active=True, code=code, user=request.user)
                for s in saleitems:
                    if s.product == product and s.sell_id == sale:
                        s.quantity += 1
                        s.total_price = int(s.total_price) + int(product.price-discount)
                        s.save()
                        return redirect(f"/sale/add/{saleid}/")
                total_price = calculate_sellitem_total_price(product.price, 1, discount)
                SellItem.objects.create(sell_id=sale, total_price=total_price, product=product, price=product.price, date=datetime.now(),
                                        quantity=1, discount=discount, user=request.user)
                return redirect(f"/sale/add/{saleid}/")

        except:
            return redirect(f"/sale/add/{saleid}/")
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def checkout(request, saleid):
    if request.user.status == "Paid":
        if request.method == "POST":
            saleitems = SellItem.objects.filter(sell_id=saleid, user=request.user)
            sale = Sell.objects.get(id=saleid, user=request.user)
            paid = float(request.POST.get('paid'))
            customer = request.POST.get('customer')
            total_price = 0
            for saleitem in saleitems:
                total_price = (total_price + (saleitem.price * saleitem.quantity))-(saleitem.discount*saleitem.quantity)
            if paid == total_price:
                sale.checkout = True
                sale.total_price = total_price
                if customer == "---------":
                    sale.client = None
                else:
                    customer = Client.objects.get(id=customer, user=request.user)
                    customer.count += 1
                    customer.sale += total_price
                    customer.save()
                    sale.client = customer
                sale.save()
                sell_items = SellItem.objects.filter(sell_id=saleid, user=request.user)
                for sell_item in sell_items:
                    product = Product.objects.get(id=sell_item.product.id, user=request.user)
                    quantity = sell_item.quantity
                    if product.quantity - float(quantity) >= 0:
                        product.quantity = product.quantity - float(quantity)
                        product.count += float(quantity)
                        product.save()
            else:
                sale.checkout = True
                sale.total_price = total_price
                if customer == "---------" and sale.total_price != paid:
                    messages.error(request, "Savatni egasi mijozlar ro'yhatiga qo'shilmagan. Shuning uchun qarzga "
                                            "berilmaydi.")
                    return redirect(f"/sale/add/{saleid}/")
                else:
                    customer = Client.objects.get(id=customer, user=request.user)
                    customer.debt = customer.debt + (float(total_price) - paid)
                    customer.save()
                    sale.client = customer
                    sale.save()
                sell_items = SellItem.objects.filter(sell_id=saleid, user=request.user)
                for sell_item in sell_items:
                    product = Product.objects.get(id=sell_item.product.id, user=request.user)
                    quantity = sell_item.quantity
                    if product.quantity - float(quantity) >= 0:
                        product.quantity = product.quantity - float(quantity)
                        product.count += float(quantity)
                        product.save()
                        sale.save()

            return redirect(f"/sale/list/")
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def sale_delete(request, saleid):
    if request.user.status == "Paid":
        sale = Sell.objects.get(id=saleid)
        saleitems = SellItem.objects.filter(sell_id=sale, user=request.user)
        for saleitem in saleitems:
            saleitem.delete()
        sale.delete()
        return redirect("/sale/list/")
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def refresh(request, saleid, tp):
    if request.user.status == "Paid":
        sale = Sell.objects.get(id=saleid, user=request.user)
        sale.total_price = tp
        sale.save()
        return redirect('/sale/list/')
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def cost_list(request):
    if request.user.status == "Paid":
        data = {
            "costs": Cost.objects.filter(user=request.user)
        }
        return render(request, "sale/list-cost.html", data)
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def refresh_page(request, pk):
    if request.user.status == "Paid":
        time.sleep(1)
        return redirect(f"/sale/cheque/{pk}/")
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def cost_create(request):
    if request.user.status == "Paid":
        if request.method=="POST":
            cost = request.POST.get("cost")
            worker = request.POST.get("worker")
            category = request.POST.get("category")
            category = CostCategory.objects.get(id=category, user=request.user)
            worker = Worker.objects.get(id=worker)
            Cost.objects.create(cost=cost, category=category, worker=worker, date=datetime.now(), user=request.user)
            return redirect('/sale/cost-list/')
        data = {
            "category": CostCategory.objects.filter(user=request.user),
            "worker": Worker.objects.filter(user=request.user)
        }
        return render(request, "sale/add-cost.html", data)
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def saleitem_list(request, s):
    if request.user.status == "Paid":
        saleitem = SellItem.objects.filter(sell_id=s, user=request.user)
        sale_item = []
        for item in saleitem:
            sale_item.append({item.id: item.quantity*(item.price-item.discount)})
        total_price = 0
        for sale in saleitem:
            total_price = int((total_price + (sale.price*sale.quantity))-(sale.discount*sale.quantity))
        data = {
            "products": Product.objects.filter(user=request.user).order_by('code'),
            "clients": Client.objects.filter(user=request.user),
            "sale": s,
            "saleitems": saleitem,
            "total_price": total_price,
            "sale_item": sale_item,

        }
        return render(request, "sale/saleitem_list.html", data)
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def return_create(request, sale, saleitem_id):
    if request.user.status == "Paid":
        if request.method == "POST" and Sell.objects.get(id=sale, user=request.user).client is not None:
            customer = request.POST.get("customer")
            customer = Client.objects.get(id=customer, user=request.user)
            quantity = request.POST.get("quantity")
            worker = request.POST.get("worker")
            item = SellItem.objects.get(id=saleitem_id, user=request.user)
            saleitems = SellItem.objects.filter(sell_id_id=sale, user=request.user)
            paid = item.price * float(quantity) - (item.discount * float(quantity))
            product = Product.objects.get(id=item.product_id, user=request.user)
            total_price = 0
            sell = Sell.objects.get(id=sale, user=request.user)
            for saleitem in saleitems:
                if saleitem.sell_id_id:

                    if float(item.quantity) >= float(quantity):
                        for saleitem in saleitems:
                            total_price = (total_price + (saleitem.price * saleitem.quantity)) - (saleitem.discount * saleitem.quantity)
                        if customer.debt == 0 and float(item.quantity) >= float(quantity):
                            sell.total_price = total_price-paid
                            item.quantity = item.quantity - float(quantity)
                            item.total_price = (item.price - item.discount) * item.quantity
                            Return.objects.create(sellitem=item,
                                            customer=customer,
                                            paid=paid,
                                            quantity=quantity,
                                            worker_id=worker, user=request.user)
                            if item.quantity == 0:
                                item.delete()
                            else:
                                item.save()
                            product.quantity = float(product.quantity) + float(quantity)
                            product.count = float(product.count) - float(quantity)
                            product.save()
                            sell.save()
                            if not SellItem.objects.filter(sell_id_id=sell, user=request.user):
                                sell.delete()
                            messages.success(request, f"Mijozga {paid} so'm to'landi")
                            return redirect("/sale/return/")

                        elif customer.debt > 0 and float(item.quantity) >= float(quantity):
                            if customer.debt - paid >= 0:
                                customer.debt = customer.debt - paid
                                customer.save()
                                sell.total_price = total_price - paid
                                print(total_price - paid)
                                item.quantity = item.quantity - float(quantity)
                                product.quantity = float(product.quantity) + float(quantity)
                                product.count = float(product.count) - float(quantity)
                                product.save()
                                sell.save()
                                if not SellItem.objects.filter(sell_id_id=sell, user=request.user):
                                    sell.delete()
                                Return.objects.create(sellitem=item,
                                                    customer=customer,
                                                    paid=0,
                                                    quantity=quantity,
                                                    worker_id=worker, user=request.user)
                                if item.quantity == 0:
                                    item.delete()
                                else:
                                    item.save()
                                    item.total_price = (item.price - item.discount) * item.quantity
                                    item.save()
                                messages.success(request, f"Mijozga 0 so'm to'landi")
                                return redirect("/sale/return/")
                            elif customer.debt - paid < 0 and float(item.quantity) >= float(quantity):
                                print(57885)
                                product.quantity = float(product.quantity) + float(quantity)
                                product.count = float(product.count) - float(quantity)
                                product.save()
                                paid = -(customer.debt - paid)
                                print("--------------------")
                                print(total_price - paid)
                                item.quantity = float(item.quantity) - float(quantity)
                                customer.debt = 0
                                Return.objects.create(sellitem_id=saleitem_id,
                                                                customer=customer,
                                                                paid=paid,
                                                                quantity=quantity,
                                                                worker_id=worker, user=request.user)


                                if item.quantity == 0:
                                    item.delete()
                                else:
                                    item.save()
                                    item.total_price = (item.price - item.discount) * item.quantity
                                    item.save()
                                customer.save()
                                sale_total_price = 0
                                if SellItem.objects.filter(sell_id_id=sell, user=request.user):
                                    for t in SellItem.objects.filter(sell_id_id=sell, user=request.user):
                                        sale_total_price += t.total_price
                                    sell.total_price = sale_total_price
                                    sell.save()

                                else:
                                    sell.delete()
                                messages.success(request, f"Mijozga {paid} so'm to'landi.")
                                return redirect("/sale/return/")
                    elif float(item.quantity) < float(quantity):
                        messages.error(request, "Berilgandan ko'p mahsulot qaytarib olinmaydi!")
                        return redirect(f"/sale/{sale}/items/")
                else:
                    sell.delete()
        elif Sell.objects.get(id=sale, user=request.user).client is None:
            messages.error(request, "Savatni egasi mijozlar ro'yhatiga qo'shilmagan.")
            return redirect(f"/sale/{sale}/items/")
        data = {
            "sale": sale,
            "saleitem": saleitem_id,
            "customers": Client.objects.filter(user=request.user),
            "staff": Worker.objects.filter(user=request.user),
        }
        return render(request, "sale/add-returns.html", data)
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def return_list(request):
    if request.user.status == "Paid":
        data = {
            "items": Return.objects.filter(user=request.user)
        }
        return render(request, "sale/list-returns.html", data)
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def category(request):
    if request.user.status == "Paid":
        name = request.POST.get("name")
        CostCategory.objects.create(name=name, user=request.user)
        return redirect("/sale/cost-list/")
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")


@login_required(login_url='/accounts/login/')
def plus(request, sale_id, saleitem_id):
    if request.user.status == "Paid":

        sellitem = SellItem.objects.get(id=saleitem_id, user=request.user)
        sellitem.quantity = sellitem.quantity + 1
        sellitem.total_price = int(sellitem.total_price) + int(sellitem.price - sellitem.discount)
        sellitem.save()
        return redirect(f"/sale/add/{sale_id}/")
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

@login_required(login_url='/accounts/login/')
def minus(request, sale_id, saleitem_id):
    if request.user.status == "Paid":
        sellitem = SellItem.objects.get(id=saleitem_id, user=request.user)
        sellitem.quantity = sellitem.quantity - 1
        sellitem.total_price = int(sellitem.total_price) - int(sellitem.price - sellitem.discount)
        sellitem.save()
        return redirect(f"/sale/add/{sale_id}/")
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")


@login_required(login_url='/accounts/login/')
def quantity(request, sale_id, saleitem_id):
    if request.user.status == "Paid":
        if request.method == "POST":
            quantity = float(request.POST.get("quantity"))
            sellitem = SellItem.objects.get(id=saleitem_id, user=request.user)
            sellitem.quantity = quantity
            sellitem.save()
            return redirect(f"/sale/add/{sale_id}/")
    else:
        return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")

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

#
# customer_debt = 100
# sale_total_price = 150
# sale_paid = 50
# return_paid = 50
# sale_total_price = sale_total_price - return_paid
# if (customer_debt-return_paid)>0:
#     customer_debt = customer_debt - return_paid
# elif sale_paid>sale_total_price-return_paid:
#     sale_paid = sale_total_price-return_paid
# elif sale_paid<sale_total_price-return_paid:
#     sale_paid = sale_paid
# print(customer_debt)
# print(sale_total_price)
# print(sale_paid)
# print(return_paid)