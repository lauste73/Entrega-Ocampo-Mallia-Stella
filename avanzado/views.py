from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from avanzado.models import Moto
from avanzado.forms import BusquedaMoto


class VerMotos(ListView):
    model = Moto
    template_name = 'avanzado/ver_motos.html'

    def get_queryset(self):
        chasis = self.request.GET.get('chasis', '')
        if chasis:
            object_list = self.model.objects.filter(chasis__icontains=chasis)
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
    
class DescMoto(DetailView):
    model = Moto
    template_name = 'avanzado/descripcion_moto.html'
