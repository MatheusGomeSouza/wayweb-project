from django.db import models
from rest_framework import viewsets
from produto.api import serialize
from produto import models

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serialize.CategoriaSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serialize.ProdutoSerializer

# class TipoPagViewSet(viewsets.ModelViewSet):
#     queryset = models.TipoPagamento.objects.all()
#     serializer_class = serialize.TipoPagSerializer

# class PedidoViewSet(viewsets.ModelViewSet):
#     queryset = models.Pedido.objects.all()
#     serializer_class = serialize.PedidoSerializer

# class EntregaViewSet(viewsets.ModelViewSet):
#     queryset = models.Entrega.objects.all()
#     serializer_class = serialize.EntregaSerializer

# class ItemPedidoViewSet(viewsets.ModelViewSet):
#     queryset = models.ItemPedido.objects.all()
#     serializer_class = serialize.ItemPedidoSerializer