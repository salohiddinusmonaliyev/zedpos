from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import CustomUser

from accounts.models import *

@login_required(login_url='/accounts/login/')
def worker(request):
    data = {
        "staff": Worker.objects.all(),
    }
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        p_num = request.POST.get("number")
        Worker.objects.create(first_name=first_name, last_name=last_name, ph_number=p_num, user=request.user)
        return redirect('/accounts/worker/')
    return render(request, "people/worker.html", data)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.status = 'Unpaid'
            user.save()
            form.save()
            print(form, user)
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password1'))
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            render(request, "register.html", {"form": form})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


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
