from rest_framework import serializers
from produto.models import Categoria, Produto

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'

class InfoProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(many=True)
    produto = ProdutoSerializer(many=True)