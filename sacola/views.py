# from django.shortcuts import get_object_or_404, redirect,render
# from django.views.decorators.http import require_POST
# from produto.models import *
# # from .cart import Cart
# from .forms import CartAddProductForm




# from random import randint
from django.shortcuts import render


def sacola_detail(request):
    if request.session.get("teste") is None:
        request.session["teste"]  = randint(1, 1000)
    return render(request, "sacola/sacola_detail.html")


# def sacola_detail(request):
#         request.session["SESSÂO ABERTA"] = {
#             "produto_1" : {
#                 "Nome": "Camiseta Polo",
#                 "Preço": 29.9,
#                 "quantidade": 3,
#             },
#              "produto_2" : {
#                 "Nome": "Calça Harmane",
#                 "Preço": 500.000,
#                 "quantidade": 1,
#             },
#             "produto3": {
#                 "Nome": "Guilherme gay",
#                 "preco": 100.00,
#                 "quantidade": 2 

#             },
#         }
#         return render(request, "sacola/sacola_detail.html")



# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)

#     form = CartProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(
#             product=product, 
#             quantity=cd["quantity"], 
#             override_quantity=cd["override"]
#         )
#     return redirect("cart:detail")

# @require_POST
# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect("cart:detail")    

# def cart_detail(request):
#     cart = Cart(request)
#     return rend(request, "cart/cart_detail.html", {"cart": cart}) 

