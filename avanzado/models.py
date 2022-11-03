from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Publicacion(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo=models.CharField(max_length=20)
    linea_texto = RichTextField(max_length=400)

    
