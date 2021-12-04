from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from produto.models import Product
from django.template.defaulttags import register
import math


from .cart import Cart
from .forms import CartAddProductForm, CartAddFreigth


@register.filter
def get_range(value):
    return range(value)

@register.filter
def div(value, div):
    return math.ceil(value / div)

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd["quantity"],
            size=cd["size"],
            size_number=cd["size_number"],
            override_quantity=cd["override"]
            
        )

    return redirect("sacola:detail")


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("sacola:detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/cart_detail.html", {"cart": cart})

@require_POST
def cart_add_freight(request):
    if request.session.get('freight') is None:
            request.session['freight'] = {}
    
    form = CartAddFreigth(request.POST)
    
    if form.is_valid():
        cart = Cart(request)
        cart.add_freight(form.data.get('cep'))

    return redirect("sacola:detail")