"""wayweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic.edit import DeleteView
from produto.api.viewsets import CategoriaViewSet, EntregaViewSet, ItemPedidoViewSet, ModeloViewSet, PedidoViewSet, ProdutoViewSet, TipoPagViewSet
from warnings import simplefilter
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from produto.api import *
from produto.views import *
from sacola.views import *
from django.conf.urls.static import static
from django.conf import settings

route = routers.DefaultRouter()

route.register('categoria', CategoriaViewSet, basename="categoria")
route.register('modelo', ModeloViewSet, basename="categoria")
route.register('prod', ProdutoViewSet, basename="categoria")
route.register('tipopag', TipoPagViewSet, basename="categoria")
route.register('pedido', PedidoViewSet, basename="categoria")
route.register('entrega', EntregaViewSet, basename="categoria")
route.register('itempedido', ItemPedidoViewSet, basename="categoria")

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('', user_views.index, name="templates/index"),
    path('reg/', user_views.gerenciamento, name="gerenciamento"),
    path('register/', user_views.register, name='register'),
    path('prod/', include(route.urls)),
    path("sacola/", include("sacola.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
