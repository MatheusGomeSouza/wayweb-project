from django.http import request
from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework import response
from rest_framework.viewsets import views, ViewSet
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from produto.api.serialize import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from rest_framework.decorators import action

@api_view(['GET', 'POST'])
def categoria_list(request,format=None):
    if request.method == 'GET':
        snippets = Categoria.objects.all()
        serializer = CategoriaSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detail(request, pk, format=None):
    try:
        cat = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializer(cat)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriaSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)