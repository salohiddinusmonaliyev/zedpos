from django.shortcuts import render

from accounts.models import CustomUser

def workers_list(request):
    data = {
        "workers": CustomUser.objects.all(),
    }
    return render(request, "worker-list.html", data)




# from rest_framework.viewsets import ModelViewSet
#
# from .models import *
# from .serializer import *
#
# # Create your views here.
# class UserViewSet(ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
