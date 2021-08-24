from django.db import models


# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

class Modelo(models.Model):
    foto = models.ImageField(upload_to= 'pic_folder/', default = 'pic_folder/None/a.png')

class Produto(models.Model):
    SKU = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cor = models.CharField(max_length=255, null=True)
    tamanho = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0)

class TipoPagamento(models.Model):
    NomeTipoPag = models.CharField(max_length=255)

class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipoPag = models.ForeignKey(TipoPagamento, on_delete=models.CASCADE)
    valorTotal = models.IntegerField()
    status = models.CharField(max_length=255)
    dataCompra = models.DateField()

class Entrega(models.Model):
    previsao = models.DateField()
    cod_status = models.IntegerField()

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    preco = models.IntegerField()
    quantidade = models.IntegerField()
