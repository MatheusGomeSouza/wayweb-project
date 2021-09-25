from django.urls import path
# from .views import sacola_detail
from .views import *

app_name = "sacola"

urlpatterns = [
    path("", sacola_detail, name="detail"), 
    # path("add/<int:product_id>/", cart_add, name="add"),
    # path("remove/<int:product_id>/", cart_remove, name="remove"),
]