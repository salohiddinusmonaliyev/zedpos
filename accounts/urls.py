from django.urls import path

from accounts.views import *

urlpatterns = [
    path('worker/', worker, name='worker'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name="register")
]
