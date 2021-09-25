from django.urls import path
from .views import detalhe_produto
from .views import *

app_name = "produto"

urlpatterns = [
    path("", detalhe_produto, name="detalhe_produto"),

]
