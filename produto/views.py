from django.shortcuts import render
import json
from rest_framework.viewsets import views, ViewSet
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from produto.models import Produto, Categoria, Peca
from produto.serialize import CategoriaSerializer, PecaSerializer, ProdutoSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from rest_framework.decorators import action

class CadastroProd(ViewSet):
    @csrf_exempt
    @action(methods=['POST'], detail=False)
    def cadCat(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def cadPeca(self, request):
        serializer = PecaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    @action(methods=['POST'], detail=False)
    def cadProd(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
