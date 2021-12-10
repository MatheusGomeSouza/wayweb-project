from django.contrib import admin
from .models import Estoque

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ["product", "size","quantity"]
    list_filter = ["product", "size"]
    list_editable = ["quantity"]
    search_fields = ["product__name"]
