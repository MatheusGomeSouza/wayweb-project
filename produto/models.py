from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

class Modelo(models.Model):
    nome = models.CharField(max_length=255, default="")

class Produto(models.Model):
    SKU = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cor = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    tamanho = models.CharField(max_length=255)

class TipoPagamento(models.Model):
    tipoPag = models.CharField(max_length=255)

class Pedido(models.Model):
    pagamento = models.ForeignKey(TipoPagamento, on_delete=models.CASCADE)
    valorTotal = models.IntegerField()
    status = models.CharField(max_length=255)
    dataCompra = models.DateField

class Entrega(models.Model):
    previsao = models.DateField()
    codStatus = models.CharField(max_length=255)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    preco = models.IntegerField()
    quantidade = models.IntegerField()