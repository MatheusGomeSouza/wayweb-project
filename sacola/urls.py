from django.urls import path, include
from .views import cart_add, cart_detail, cart_remove
from django.conf import settings
import debug_toolbar

app_name = "sacola"

urlpatterns = [
    path("", cart_detail, name="detail"),
    path("add/<int:product_id>/", cart_add, name="add"),
    path("remove/<int:product_id>/", cart_remove, name="remove"),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls)),]
