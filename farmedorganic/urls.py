from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home,  name='home'),
    path('accounts/profile', views.profile,  name='profile'),
    path('shop', ShopView.as_view(),  name='shop'),
    path('shop/', SearchResultView.as_view(),  name='shop_search'),
    path('sell', views.CreateProduct,  name='create-product'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
