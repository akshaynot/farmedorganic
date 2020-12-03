from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cart,  name='cart'),
    path('<slug>/add-to-cart/', views.add_to_cart,  name='add-to-cart'),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
