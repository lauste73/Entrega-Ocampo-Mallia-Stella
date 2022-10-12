from django.urls import path
from home1 import views

urlpatterns = [
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('ver-usuario/', views.ver_usuarios, name='ver_usuarios'),
    path('', views.home, name='home'),
]
