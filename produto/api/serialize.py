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

# class TipoPagSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = TipoPagamento
#         fields = '__all__'

# class PedidoSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Pedido
#         fields = '__all__'

# class EntregaSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Entrega
#         fields = '__all__'

# class ItemPedidoSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ItemPedido
#         fields = '__all__'