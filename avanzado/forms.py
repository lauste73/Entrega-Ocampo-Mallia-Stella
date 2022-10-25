from django import forms




class Moto(forms.Form):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    chasis = forms.CharField(max_length=20)
    estado = forms.CharField(max_length=20)
    contacto = forms.IntegerField()
    
    
class BusquedaMoto(forms.Form):
    chasis = forms.CharField(max_length=20, required=False)