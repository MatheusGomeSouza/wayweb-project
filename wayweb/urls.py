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

import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import produto
from users import views as user_views
from django.contrib.auth import views as auth_views
from sacola.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles import *
from django.urls import path, include


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('', user_views.index, name="guest/index"),
    path('masculino', user_views.masculino, name="guest/masculino"),
    path('produto', user_views.produto, name="guest/descricao"),
    path('compra', user_views.compra, name="guest/compra"),
    path('pagamento', user_views.pagamento, name="guest/pagamento"),
    path('reg/', user_views.gerenciamento, name="gerenciamento"),
    path('register/', user_views.register, name='register'),
    path("sacola/", include("sacola.urls")),
    path('product/', include('produto.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# DEBUG TOOLBAR
if settings.DEBUG:
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls)),]
