from django import forms
from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField
    
class FormularioPublicacion(forms.Form):
    titulo = forms.CharField(max_length=20)
    subtitulo=forms.CharField(max_length=20)
    linea_texto = RichTextFormField(max_length=400)
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaPublicacion(forms.Form):
    titulo = forms.CharField(max_length=20, required = False)
    
