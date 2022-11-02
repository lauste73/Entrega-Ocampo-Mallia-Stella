from django import forms

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
    linea_texto = forms.CharField(max_length=300)
    
class BusquedaPublicacion(forms.Form):
    nombre = forms.CharField(max_length=30, required = False)
    
