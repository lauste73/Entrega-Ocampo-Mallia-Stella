from django.urls import path
from avanzado import views

urlpatterns = [
    
    #MOTOS(SECCION DE LA TIENDA)
    path('motos/',views.VerMotos.as_view(), name='ver_motos'),
    path('motos/crear/',views.CrearMoto.as_view(), name='crear_moto'),
    path('motos/editar/<int:pk>', views.EditarMoto.as_view(), name='editar_moto'),
    path('motos/eliminar/<int:pk>', views.EliminarMoto.as_view(), name='eliminar_moto'),
    path('motos/descripcion/<int:pk>', views.DescMoto.as_view(), name='descripcion_moto'),
    
    #POSTEOS(SECCION DE LAS PUBLICACIONES)
    
    path('crear-publicacion/',views.crear_publicacion, name='crear_publicacion'),
    path('ver-publicacion/',views.ver_publicaciones, name='ver_publicaciones'),
    


  
]
