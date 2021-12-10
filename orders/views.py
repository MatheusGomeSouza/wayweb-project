import mercadopago
import urllib
import urllib.request
import xmltodict

from pprint import pprint
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse
from django.views.generic import CreateView
from payments.models import Payment

from sacola.cart import Cart

from .forms import OrderCreateForm
from .models import Item, Order
from inventory.models import Estoque


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm

    def form_valid(self, form):
        cart = Cart(self.request)
        if cart:
            cd = form.cleaned_data

            order = Order.objects.create(
                user = cd['user'],
                cpf = cd["cpf"],
                name = cd['name'],
                email = cd['email'],
                postal_code = cd['postal_code'],
                address = cd['address'],
                number = cd['number'],
                complement = cd['complement'],
                district = cd['district'],
                state = cd['state'],
                city = cd['city'],
            )

            for item in cart:
                Item.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                    size=item["size"],
                )
                est = Estoque.objects.get(product_id=item["product"], size=item["size"])
                est.quantity -= item["quantity"]
                est.save()

            frete = cart.get_freigth()
            order.freight = frete
            order.save()

            cart.clear()

            mp = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)

            payment_data = {
                "transaction_amount": float(order.get_total_price()),
                "token": cd["token"],
                "description": order.get_description(),
                "installments": int(cd["installments"]),
                "payment_method_id": cd["payment_method_id"],
                "payer": {
                    "email": cd["email"],
                    "identification": {"type": "CPF", "number": cd["doc_number"]},
                },
            }

            payment = mp.payment().create(payment_data)
            
            if payment["status"] == 201:
                if payment["response"]["status"] == "approved":
                    order.paid = True
                    order.save()
                    Payment.objects.create(
                        order = order,
                        transaction_amount = float(order.get_total_price()),
                        installments = cd['installments'],
                        payment_method_id = cd['payment_method_id'],
                        email = cd['email'],
                        doc_number = cd['doc_number'],
                        mercado_pago_id = payment["response"]["id"],
                        mercado_pago_status = payment["response"]["status"],
                        mercado_pago_status_detail = payment["response"]["status_detail"],
                    )

            return redirect('my_orders')
        return HttpResponseRedirect(reverse("pages:home"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        context["publishable_key"] = settings.MERCADO_PAGO_PUBLIC_KEY
        return context