from django.template import Template, Context
from django.shortcuts import render, redirect
from home1.models import Usuario
from home1.forms import FormularioUsuario, BusquedaUsuario
from datetime import datetime

def crear_usuario(request):
    if request.method == 'POST':
        
        formulario = FormularioUsuario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_creacion = data.get('fecha_creacion', datetime.now())
            
            usuario = Usuario(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion=fecha_creacion)
            usuario.save()
            
            return redirect('ver_usuarios')
        
    formulario = FormularioUsuario()
    
    return render(request, 'home/crear_usuario.html', {'formulario': formulario})


def ver_usuarios(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        usuario = Usuario.objects.filter(nombre__icontains=nombre)
    else:
        usuarios = Usuario.objects.all()
    
    formulario = BusquedaUsuario()
    
    return render(request, 'home/ver_usuarios.html', {'usuarios': usuarios, 'formulario': formulario})