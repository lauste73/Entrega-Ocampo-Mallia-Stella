from django.urls import path
from avanzado import views

urlpatterns = [
    path('crear-publicacion/', views.CrearPublicacion.as_view(), name='crear_publicacion'),
    path('ver-publicaciones/', views.ListaPublicacion.as_view(), name='ver_publicaciones'),
    path('publicacion/descripcion/<int:pk>', views.DescPublicacion.as_view(), name='descripcion_publicacion'),
    path('publicacion/eliminar/<int:pk>', views.EliminarPublicacion.as_view(), name='eliminar_publicacion'),
    path('publicacion/editar/<int:pk>', views.EditarPublicaion.as_view(), name='editar_publicacion'),
    
]
