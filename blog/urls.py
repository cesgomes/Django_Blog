# Passo 2: Criar este arquivo e importar a URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
]
