from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import ShopView , SearchResultView , SellersView , UpdateProductView
from . import views

urlpatterns = [
    path('', views.home,  name='home'),
    path('accounts/profile', views.profile,  name='profile'),
    path('shop', ShopView.as_view(),  name='shop'),
    path('shop/', SearchResultView.as_view(),  name='shop-search'),
    path('myproducts/', SellersView.as_view(), name='selling'),
    path('myproducts/<slug>', UpdateProductView.as_view(), name='edit-product'),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
