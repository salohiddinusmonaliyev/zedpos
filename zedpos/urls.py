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
from django.urls import path

from app.views import dashboard
from product.views import product_list
from sell.views import sale_list, sale_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:a>/<str:b>/', dashboard),
    path('', dashboard),
    path('product-list/', product_list),
    path('sale-list/s', sale_list),
    path("saleadd/", sale_add),
]
