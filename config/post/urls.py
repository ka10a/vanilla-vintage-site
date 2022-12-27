from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index, contacts, products, about, redirect_to_index

urlpatterns = [
    path('', redirect_to_index),
    path('index/', index, name="index"),
    path('contacts/', contacts, name="contacts"),
    path('products/', products, name="products"),
    path('about/', about, name="about"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
