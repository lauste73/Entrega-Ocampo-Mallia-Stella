from django import forms

class FormularioUsuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaUsuario(forms.Form):
    nombre = forms.CharField(max_length=30, required = False)
    
class FormularioChat(forms.Form):
    autor = forms.CharField(max_length= 20)
    mensaje = forms.CharField(max_length=150)
    

    