from django import forms

class FormularioUsuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaUsuario(forms.Form):
    nombre = forms.CharField(max_length=30, required = False)
    
class FormularioChat(forms.Form):
    mensaje = forms.CharField(max_length=150)
    
# Lo de acá abajo va a ser lo que vaya como template para crear publicaciones, se puede hacer con login required o mixin
 
class FormularioPublicacion(forms.Form):
    ...
    

    