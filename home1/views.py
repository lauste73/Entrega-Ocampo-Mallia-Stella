from django.template import Template, Context
from django.shortcuts import render, redirect
from home1.models import Usuario, Chat
from home1.forms import FormularioUsuario, BusquedaUsuario, FormularioChat
from datetime import datetime

def crear_usuario(request):
    if request.method == 'POST':
        
        formulario = FormularioUsuario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_creacion = data['fecha_creacion'] or datetime.now()
            
            usuario = Usuario(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion=fecha_creacion)
            usuario.save()
            
            return redirect('ver_usuarios')
        
    formulario = FormularioUsuario()
    
    return render(request, 'home/crear_usuario.html', {'formulario': formulario})


def ver_usuarios(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
    else:
        usuarios = Usuario.objects.all()
    
    formulario = BusquedaUsuario()
    
    return render(request, 'home/ver_usuarios.html', {'usuarios': usuarios, 'formulario': formulario})

def chat(request):
    if request.method == 'POST':
        
        formulario = FormularioChat(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            mensaje = data['mensaje']
            
            chat = Chat(mensaje=mensaje)
            chat.save()
            
            return redirect('chat')
        
    formulario = FormularioChat()
    
    return render(request, 'home/chat.html', {'formulario': formulario})


def home(request):
    return render(request, 'home/home.html', {})

def sobre_nosotros(request):
    return render(request, 'home/sobre_nosotros.html', {} )

