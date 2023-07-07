from django.shortcuts import render,redirect
from .models import Producto
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    objeto = Producto.objects.all()
    return render(request, 'index.html', {'objeto':objeto})

def login(request):
    return render(request,'login.html')

def logout(request):
    return logout_then_login(request, login_url="login")

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
       registro = Registro()
       return render(request,'registro.html',{'form':registro})

def perfiles(request):
    return render(request,'crudperfil.html')
def producto(request):
    return render(request,'crudprod.html')
def logout(request):
    return logout_then_login(request,login_url="login")