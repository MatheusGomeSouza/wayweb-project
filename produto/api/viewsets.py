from django.db import models
from rest_framework import viewsets
from produto.api import serialize
from produto import models

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serialize.CategoriaSerializer
    
class ModeloViewSet(viewsets.ModelViewSet):
    queryset = models.Modelo.objects.all()
    serializer_class = serialize.ModeloSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serialize.ProdutoSerializer

class TipoPagViewSet(viewsets.ModelViewSet):
    queryset = models.TipoPagamento.objects.all()
    serializer_class = serialize.TipoPagSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = models.Pedido.objects.all()
    serializer_class = serialize.PedidoSerializer

class EntregaViewSet(viewsets.ModelViewSet):
    queryset = models.Entrega.objects.all()
    serializer_class = serialize.EntregaSerializer

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = models.ItemPedido.objects.all()
    serializer_class = serialize.ItemPedidoSerializer