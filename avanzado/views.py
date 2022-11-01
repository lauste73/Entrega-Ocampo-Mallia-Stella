from asyncio.windows_events import NULL
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from avanzado.models import Moto, Publicacion
from avanzado.forms import BusquedaMoto, Publicacion
from django.contrib.auth.decorators import login_required

class VerMotos(ListView):
    model = Moto
    template_name = 'avanzado/ver_motos.html'

    def get_queryset(self):
        marca = self.request.GET.get('marca','')
        if marca:
            object_list = self.model.objects.filter(marca__icontains=marca)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaMoto()
        return context
    
 
class CrearMoto(LoginRequiredMixin, CreateView):
    model = Moto
    success_url = '/avanzado/motos/'
    template_name = 'avanzado/crear_moto.html'
    fields = ['modelo', 'marca', 'color', 'chasis','estado','contacto']
    

class EditarMoto(LoginRequiredMixin, UpdateView):
    model = Moto
    success_url = '/avanzado/motos/'
    template_name = 'avanzado/editar_moto.html'
    fields = ['modelo', 'marca', 'color', 'chasis','estado','contacto']
    

class EliminarMoto(LoginRequiredMixin, DeleteView):
    model = Moto
    success_url = '/avanzado/motos/'
    template_name = 'avanzado/eliminar_moto.html'
    

class DescMoto(LoginRequiredMixin,DetailView):
    model = Moto
    template_name = 'avanzado/descripcion_moto.html'

class CrearPublicacion(LoginRequiredMixin,CreateView):
    model = Publicacion
    success_url = 'home/'
    template_name = 'avanzado/crear_publicacion.html'
    fields = ['titulo', 'linea_texto']
