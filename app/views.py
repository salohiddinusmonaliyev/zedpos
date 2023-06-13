from django.db.models import Sum
from django.shortcuts import render, redirect

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
def dashboard(request, a=None, b=None):
    if a==None and b==None:
        a = str(datetime.date.today())
        b = str(datetime.date.today())
    total_price = 0
    #sales
    sales = Sell.objects.filter()
    sales_count = 0
    for s in sales:
        if str(s.time.date())>=a and str(s.time.date())<=b:
            if s.total_price==None:
                total_price+=0
            else:
                total_price=int(s.total_price)+int(total_price)
                sales_count = sales_count + 1
    #kam qolgan
    kam = Product.objects.filter(is_active=True, quantity__lte=10)

    #products
    products = Product.objects.filter(is_active=True)
    products_price = 0
    my_list = []
    for p in products:
        products_price = products_price + (p.arrival_price * p.quantity)
        my_list.append(p.count)

    #foyda
    data = SellItem.objects.filter()
    foyda = 0
    for i in data:
        if str(i.date.date()) >= a and str(i.date.date()) <= b:
            # print(i.product)
            product_price = (int(i.quantity) * i.product.price)
            # print(product_price)
            product_kelgan = (int(i.quantity) * i.product.arrival_price)
            discount = (int(i.quantity) * i.discount)
            # print(product_kelgan)
            foyda = foyda + int(product_price - product_kelgan - discount)
    dealers = Payment.objects.filter()
    pay = 0
    for p in dealers:
        pay += p.payment

    customers = Client.objects.all()
    debtors = Client.objects.filter(debt__gte=1)

    costs = Cost.objects.filter()
    cost = 0
    for c in costs:
        if str(c.date.date()) >= a and str(c.date.date()) <= b:
            cost+=c.cost

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
        if item == None:
            totalprice.append(0)
        else:
            totalprice.append(item)
    for item in calculate_total_cost(lists):
        dates.append(f"{item}")
    # print(dates)

    top_products = Product.objects.all().order_by('count')[:5]

    # Prepare data for the chart
    labels = [wa.name for wa in top_products]
    values = [la.count for la in top_products]
    print(values)

    data = {
        "kam": kam,
        "sales": sales,
        "sale_count": sales_count,
        "total_price": total_price-pay,
        "products": products.count(),
        "products_price": products_price,
        "customers": customers.count(),
        "debtors": debtors.count(),
        "cost": cost,
        "foyda": foyda,
        "dates": dates,
        "a": a,
        "b": b,
        "top": Product.objects.all().order_by('count')[:5],
        # "chart": calculate_total_cost(lists),
        "data_points": totalprice,
        'data': {'labels': labels,
                'values': values,}
    }
    return render(request, "index.html", data)

def date_range(request):
    if request.method == "POST":
        a = request.POST.get('a')
        b = request.POST.get('b')
        # yesterday = request.POST.get("yesterday")
        # today = request.POST.get("today")
        # week = request.POST.get("week")
        # day30 = request.POST.get("30day")
        # month = request.POST.get("month")
        # current_month = datetime.datetime.now().month
        # print(current_month)
        return redirect(f"/dashboard/{a}/{b}/")

# class Archive(APIView):
#     def get(self, request):
#         product = Product.objects.filter(is_active=False)
#         ser = ProductSerializer(product, many=True)
#         return Response(ser.data)