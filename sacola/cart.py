# from decimal import Decimal
# import copy
# from produto.models import *





# class Cart:
#     def __init__(self, request):
#         if request.session.get("cart") is None:
#             request.session["cart"] = {}

#         self.cart = request.session["cart"]
#         self.session = request.session

#     def __iter__(self):
#         cart = copy.deepcopy(self.cart)

#         products = Produto.objects.filter(id__in=cart)
#         for produto in products:
#             cart[str(produto.id)]["produto"] = produto

#         for item in cart.values():
#             item['preco'] = Decimal(item['preco'])
#             item['total_price'] = item['preco'] * item["quantidade"]
#             yield item

#     def __len__(self):
#         return sum(item['quantidade'] for item in self.cart.values())

#     def add(self, product, quantity=1, override_quantity=False):
#         product_id = str(product.id)

#         if product_id not in self.cart:

#             self.cart[product_id] = {
#                 "quantidade": 0,
#                 "preco": str(product.price),
#             }

#         if override_quantity:
#             self.cart[product_id]["quantidade"] = quantity
#         else:
#             self.cart[product_id]["quantidade"] += quantity

#         self.session.modified = True
#         self.save()

#     def remove(self, product):
#         product_id = str(product.id)

#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save()

#     def save(self):
#         self.session.modified = True