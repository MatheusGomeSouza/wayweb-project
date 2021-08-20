from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

class Peca(models.Model):
    tamanho = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)
    gereno = models.CharField(max_length=255, null=True, blank=True)

class Produto(models.Model):
    SKU = models.CharField(max_length=255)
    preco = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
