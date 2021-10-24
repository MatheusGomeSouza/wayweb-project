from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import UserRegisterForm
from .models import *

# Create your views here.

@csrf_protect
def index(request):
    return render(request,'guest/index.html')

def masculino(request):
    return render(request, 'guest/masculino.html')

def produto(request):
    return render(request, 'guest/descricao.html')

def compra(request):
    return render(request, 'guest/compra.html')

def pagamento(request):
    return render(request, 'guest/pagamento.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

def gerenciamento(request):
    return render(request, "produto.html")