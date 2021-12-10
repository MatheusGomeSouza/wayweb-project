import copy
from decimal import Decimal
import decimal
import urllib
import urllib.request
import xmltodict


from django.conf import settings
from produto.models import Product

from .forms import CartAddProductForm


class Cart:
    def calcularFrete(self, detino, numero_de_produtos):
        params = urllib.parse.urlencode({
        'sCepOrigem': '08551300',
        'sCepDestino': detino,
        'nVlPeso': numero_de_produtos * 0.2,
        'nVlComprimento': 15,
        'nVlAltura': 15,
        'nVlLargura': 15,
        'nCdServico': '04014'})

        url = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?" + params + "&nCdEmpresa=&sDsSenha=&sCdAvisoRecebimento=n&sCdMaoPropria=n&nVlValorDeclarado=0&nVlDiametro=0&StrRetorno=xml&nIndicaCalculo=3&nCdFormato=1&?"

        response = urllib.request.urlopen(url)

        data = response.read()

        response.close()

        data = xmltodict.parse(data)

        return data['Servicos']['cServico']['Valor']

    def __init__(self, request):
        if request.session.get(settings.CART_SESSION_ID) is None:
            request.session[settings.CART_SESSION_ID] = {}

        self.cart = request.session[settings.CART_SESSION_ID]
        self.session = request.session

    def __iter__(self):
        cart = copy.deepcopy(self.cart)

        products = Product.objects.filter(id__in=cart)
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["quantity"] * item["price"]
            item["update_quantity_form"] = CartAddProductForm(
                initial={"quantity": item["quantity"], "override": True}
            )

            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def add(self, product, quantity=1,size='', override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(product.price),
                "size":size,
            }

        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.cart[product_id]["quantity"] = min(20, self.cart[product_id]["quantity"])

        self.save()

    def add_freight(self, cep):
        self.session['freight']['cep'] = cep
        self.session['freight']['freight'] =  self.calcularFrete(cep.replace('-', ''),len(self.cart)).replace(',', '.')

        self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        freigth = self.get_freigth()

        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        ) + decimal.Decimal(freigth)

    def get_sub_total(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def get_freigth(self):
        if self.session.get('freight') is None:
            return '0.00'

        if 'freight' in self.session['freight']:
            return self.session['freight']['freight']
        else:
            return '0.00'

    def get_cep(self):
        if self.session.get('freight') is None:
            return ''
        
        if 'cep' in self.session['freight']:
            return self.session['freight']['cep']
        else:
            return ''

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        del self.session['freight']
        self.save()
        
    def save(self):
        self.session.modified = True