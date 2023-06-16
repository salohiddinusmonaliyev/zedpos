from django.shortcuts import render, redirect

from accounts.models import *

def worker(request):
    data = {
        "staff": Worker.objects.all(),
    }
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        p_num = request.POST.get("number")
        Worker.objects.create(first_name=first_name, last_name=last_name, ph_number=p_num)
        return redirect('/worker/')
    return render(request, "people/worker.html", data)

# def worker_create(request):
#     return render(request, "people/worker-create.html")



# from rest_framework.viewsets import ModelViewSet
#
# from .models import *
# from .serializer import *
#
# # Create your views here.
# class UserViewSet(ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
