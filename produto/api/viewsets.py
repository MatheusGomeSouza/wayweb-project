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