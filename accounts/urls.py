from django.urls import path

from accounts.views import *

urlpatterns = [
    path('', worker),
    # path('create/', worker_create),
]
