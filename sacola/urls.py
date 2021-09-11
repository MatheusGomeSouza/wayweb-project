from django.urls import path
from .views import sacola_detail

app_name = "sacola"

urlpatterns = [
    path("", sacola_detail, name="detail")
]