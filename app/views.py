from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from dealer.models import Payment
from product.models import *
from clients.models import *
from sell.models import *
import datetime


def calculate_total_cost(lists):
    total_cost_by_date = {}

    for item in lists:
        date, cost = item[0].date(), item[1]

        if date in total_cost_by_date:
            total_cost_by_date[date] += cost
        else:
            total_cost_by_date[date] = cost

    return total_cost_by_date


# Create your views here.
# @login_required(login_url='/accounts/login/')
def dashboard(request, a=None, b=None, c=None):
    if request.user.is_authenticated:
        if request.user.status == "Paid":
            if not (not (a is None) or not (b is None)):
                a = str(datetime.date.today())
                b = str(datetime.date.today())
            if c is not None:
                end_date = datetime.date.today()
                start_date = end_date - datetime.timedelta(days=c)
                a = str(start_date)
                b = str(end_date)
                print(a, b)
            total_price = 0
            # sales
            sales = Sell.objects.filter(user=request.user)
            sales_count = 0
            for s in sales:
                if a <= str(s.time.date()) <= b:
                    if s.total_price is None:
                        total_price += 0
                    else:
                        total_price = int(s.total_price) + int(total_price)
                        sales_count = sales_count + 1
            # kam qolgan
            kam = Product.objects.filter(is_active=True, quantity__lte=10, user=request.user)

            # products
            products = Product.objects.filter(is_active=True, user=request.user)
            products_price = 0
            my_list = []
            for p in products:
                products_price = products_price + (p.arrival_price * p.quantity)
                my_list.append(p.count)

            # foyda
            data = SellItem.objects.filter(user=request.user)
            foyda = 0
            for i in data:
                if a <= str(i.date.date()) <= b:
                    # print(i.product)
                    product_price = (int(i.quantity) * i.product.price)
                    # print(product_price)
                    product_kelgan = (int(i.quantity) * i.product.arrival_price)
                    discount = (int(i.quantity) * i.discount)
                    # print(product_kelgan)
                    foyda = foyda + int(product_price - product_kelgan - discount)
            dealers = Payment.objects.filter(user=request.user)
            pay = 0
            for p in dealers:
                pay += p.payment

            customers = Client.objects.filter(user=request.user)
            debtors = Client.objects.filter(debt__gte=1, user=request.user)

            costs = Cost.objects.filter(user=request.user)
            cost = 0
            for c in costs:
                if a <= str(c.date.date()) <= b:
                    cost += c.cost

            # date_list = []

            start_date = datetime.datetime.strptime(a, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(b, '%Y-%m-%d').date()

            # current_date = start_date
            # while current_date <= end_date:
            #     date_list.append(current_date)
            #     current_date += datetime.timedelta(days=1)
            lists = []
            date_range = [start_date + datetime.timedelta(days=i) for i in range((end_date - start_date).days + 1)]
            for date in date_range:
                for sale in sales:
                    if sale.time.date() == date:
                        lists.append([sale.time, sale.total_price])
                        # lists.append()
            dates = []
            totalprice = []
            for item in calculate_total_cost(lists).values():
                if item is None:
                    totalprice.append(0)
                else:
                    totalprice.append(item)
            for item in calculate_total_cost(lists):
                dates.append(f"{item}")
            # print(dates)

            top_products = Product.objects.filter(is_active=True, user=request.user).order_by('count')[:5]
            # for t in Product.objects.filter().order_by('count')[:5]:
            # if str(c.date.date()) >= a and str(c.date.date()) <= b:

            # Prepare data for the chart
            labels = [wa.name for wa in top_products]
            values = [la.count for la in top_products]

            data = {
                "kam": kam,
                "sales": sales,
                "sale_count": sales_count,
                "total_price": total_price - pay,
                "products": products.count(),
                "products_price": products_price,
                "customers": customers.count(),
                "debtors": debtors.count(),
                "cost": cost,
                "foyda": foyda,
                "dates": dates,
                "a": a,
                "b": b,
                "top": Product.objects.filter(is_active=True, user=request.user).order_by('-count')[:5],
                # "chart": calculate_total_cost(lists),
                "data_points": totalprice,
                'data': {'labels': labels,
                         'values': values, }
            }
            return render(request, "index.html", data)
        else:
            return HttpResponse("<h1>Iltimos sayt uchun to'lov qiling. Ma'lumot uchun +998XXXXXXXXX</h1>")
    else:
        return render(request, "home.html")


def date_range(request):
    if request.method == "POST":
        a = request.POST.get('a')
        b = request.POST.get('b')

        week = request.POST.get("week")
        month = request.POST.get("30day")
        year = request.POST.get("year")
        c = 0
        if week or month or year:
            if week:
                c = week
            elif month:
                c = month
            elif year:
                c = year
            return redirect(f"/dashboard/{c}/")

        return redirect(f"/dashboard/{a}/{b}/")

# class Archive(APIView):
#     def get(self, request):
#         product = Product.objects.filter(is_active=False)
#         ser = ProductSerializer(product, many=True)
#         return Response(ser.data)
