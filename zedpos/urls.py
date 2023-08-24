"""
URL configuration for zedpos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app.views import *
from clients.views import *
from product.views import *
from sell.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/<str:a>/<str:b>/', dashboard, name="dashboard"),
    path('', dashboard),
    path('product/', include('product.urls')),
    path('customers/', clients_list, name="customers"),
    path('customers-add/', customer_add, name="customer-add"),
    path('customer-delete/<int:i>/', customer_delete),
    path('debt-payment/', debt_payment),
    path('sale/', include('sell.urls')),
    path('dealers/', include('dealer.urls')),
    path('customer/<int:i>/', customer_history),
    path('date-range/', date_range),
    path('accounts/', include('accounts.urls')),
]
