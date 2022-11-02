from django import forms
from ckeditor.fields import RichTextFormField

class Moto(forms.Form):
    imagen = forms.ImageField(required=False)
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    chasis = forms.CharField(max_length=20)
    estado = forms.CharField(max_length=20)
    contacto = forms.IntegerField()

    
class BusquedaMoto(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    
class FormularioPublicacion(forms.Form):
    titulo = forms.CharField(max_length=20)
    linea_texto = RichTextFormField(max_length=400)
    
class BusquedaPublicacion(forms.Form):
    titulo = forms.CharField(max_length=20, required = False)
    
