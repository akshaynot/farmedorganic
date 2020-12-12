from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sell', views.CreateProduct,  name='create-product'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)