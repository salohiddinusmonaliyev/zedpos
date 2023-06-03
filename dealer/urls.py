from django.urls import path, include
from .views import *

urlpatterns = [
    path('', list),
    path('add/', add),
    path('payment/', payment),
]