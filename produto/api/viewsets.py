from django.db import models
from rest_framework import viewsets
from produto.api import serialize
from produto import models

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serialize.CategoriaSerializer
    

