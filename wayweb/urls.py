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
from produto.api.viewsets import CategoriaViewSet
from warnings import simplefilter
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
# from produto.views import CadastroProd
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from produto.api import *

#router = SimpleRouter()
route = routers.DefaultRouter()

route.register('cad', CategoriaViewSet, basename="categoria")

# router.register('cad', CadastroProd, 'cadastro_produto')


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('', user_views.index, name="index"),
    path('register/', user_views.register, name='register'),
    path('prod/', include(route.urls))
]

