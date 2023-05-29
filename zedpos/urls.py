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
from product.views import *
from sell.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/<str:a>/<str:b>/', dashboard),
    path('', dashboard),
    path('product-list/', product_list),
    path('sale-list/', sale_list),
    path('sale-add/<int:s>/', sale_add),
    path('sale-add/', create_sale),
    path('<int:saleid>/delete/<int:id>/', saleitem_delete),
    path('<int:saleid>/add/', saleitem_create),
    path('<int:saleid>/checkout/<int:total_price>/', checkout),
    path('<int:saleid>/delete/', sale_delete),
    path('product-add/', product_add_page),
    path('product-create/', product_add),
    path('archive/', archive),
]
