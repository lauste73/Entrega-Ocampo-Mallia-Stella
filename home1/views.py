from django.template import Template, Context
from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html', {})

def sobre_nosotros(request):
    return render(request, 'home/sobre_nosotros.html', {} )

