from rest_framework import serializers
from produto.models import Categoria, Peca, Produto

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'

class PecaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Peca
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'

class InfoProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(many=True)
    peca = PecaSerializer(many=True)
    produto = ProdutoSerializer(many=True)