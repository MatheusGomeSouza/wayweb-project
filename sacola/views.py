from django.shortcuts import get_object_or_404, redirect,render
from django.views.decorators.http import require_POST
from produto.models import Produto
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = CartProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product, 
            quantity=cd["quantity"], 
            override_quantity=cd["override"]
        )
    return redirect("cart:detail")

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:detail")    

def cart_detail(request):
    cart = Cart(request)
    return rend(request, "cart/cart_detail.html", {"cart": cart}) 

def sacola_detail(request):
    return render(request, "sacola/sacola_detail.html")
