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

from product.views import *

urlpatterns = [
    path('list/', product_list),
    path('add/', product_add_page),
    path('create/', product_add),
    path('archive/', archive),
    path('archive/<int:a>/', archive),
    path('archive-delete/<int:a>/', archive_delete),
    path('measurement/', measurements),
    path('measurement/add/', measurement_add),
    path('<int:id>/edit/', product_edit),
    path('list/', warehouse),
    path('<int:a>/add/', warehouse_add),
    path('product-add/', warehouse_add),
    path('items/<int:pk>/', product_item),
    path('unarchive/<int:pk>/', unarchive),
]
