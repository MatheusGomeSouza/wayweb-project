from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator

from produto.models import Category, Product
from .forms import UserRegisterForm
from .models import *

# Create your views here.

@csrf_protect
def index(request):
    product_list = Product.objects.all().order_by('created')[:9]

    return render(request,'guest/index.html', {'product_list': product_list})

def masculino(request):
    product_list = Product.objects.all()
    selectedCategories = request.GET.get('categories')

    if selectedCategories:
        selectedCategories = selectedCategories.split(',')
        product_list = product_list.filter(category_id__in = selectedCategories)

    paginator = Paginator(product_list, 9)   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()


    return render(request, 'guest/masculino.html', {'product_list': page_obj, 'categories' : categories, 'selectedCategories' : selectedCategories})

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