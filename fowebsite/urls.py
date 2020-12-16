from django.contrib import admin
from django.urls import path ,include
from django.conf import settings # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('farmedorganic.urls')),
    path('home/',include('farmedorganic.urls')),
    path('', include('cart.urls')),
    path('products/', include('products.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)