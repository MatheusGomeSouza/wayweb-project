from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField
from model_utils.models import TimeStampedModel

from produto.models import Product

class Estoque(TimeStampedModel):
    product = models.ForeignKey(Product, related_name="produto", on_delete=models.CASCADE, default="")
    size_choice = (
        ('1','P'),
        ('2','M'),
        ('3','G'),
        ('4','GG'),
        )
    size = models.CharField("Tamanho", max_length=2,blank=True, choices=size_choice, default="")
    quantity = models.IntegerField()

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Estoque {self.id}"