from django.contrib import admin
from django.urls import path ,include
from django.settings import static 
urlpatterns = [
]+urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)