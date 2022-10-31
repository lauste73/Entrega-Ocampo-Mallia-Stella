from django.urls import path
from home1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('ver-usuario/', views.ver_usuarios, name='ver_usuarios'),
    path('chat/', views.chat, name='chat'),
    path('about/', views.sobre_nosotros, name='sobre_nosotros'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)