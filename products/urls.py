from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sell', views.CreateProduct,  name='create-product'),
    path('details', views.ProductDetailView,  name='product-detail'),
    path('update', views.UpdateProductView,  name='update-product'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)