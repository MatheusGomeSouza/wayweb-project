from rest_framework import serializers
from produto.models import *

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'