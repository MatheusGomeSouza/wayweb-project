import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from sacola.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles import *
from django.urls import path, include

app_name = "wayweb"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', user_views.index, name="index"),
    path('masculino/', user_views.masculino, name="masculino"),
    path('produto/', user_views.produto, name="descricao"),
    path('compra/', user_views.compra, name="compra"),
    path('pagamento/', user_views.pagamento, name="pagamento"),
    path('reg', user_views.gerenciamento, name="gerenciamento"),
    path('register', user_views.register, name='register'),
    path("sacola", include("sacola.urls")),
    path('product', include('produto.urls')),
    path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# DEBUG TOOLBAR
if settings.DEBUG:
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls)),]
