from django.urls import path, include
from produto.api.viewsets import CategoryViewSet, ProductViewSet
from .views import *
# from .views import ProductDetailView, ProductListView
from rest_framework import routers

app_name = "produto"

route = routers.DefaultRouter()

route.register('categoria', CategoryViewSet, basename="categoria")
route.register('product', ProductViewSet, basename="categoria")

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", ProductListView.as_view(), name="list_by_category"),
    path('cadastro/', include(route.urls)),
]