from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField

# Create your models here.

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("produto:list_by_category", kwargs={"slug": self.slug})


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name="produto", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="produto/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("produto:detail", kwargs={"slug": self.slug})


# class TipoPagamento(models.Model):
#     tipoPag = models.CharField(max_length=255)

# class Entrega(models.Model):
#     previsao = models.DateField()
#     codStatus = models.CharField(max_length=255)
#     pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)


# class ItemPedido(models.Model):
#     produto = models.ForeignKey(Product, on_delete=models.CASCADE)
#     pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
#     preco = models.IntegerField()
#     quantidade = models.IntegerField()
