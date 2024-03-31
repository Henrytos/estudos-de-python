from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

def home(request):
    if request.method == "POST":
        username = request.POST['usuario']
        password = request.POST['senha']
        # Autenticando
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            messages.success(request, 
                "Login realizado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, 
                "Erro na autenticação. Tente novamente!")
            return redirect('home')
    else:
        return render(request, 'home.html')

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"logout feito com sucesso")
    return redirect('home')
    
def sobre(request):
    pass

def register_user(request):
    return render(request,'register.html')