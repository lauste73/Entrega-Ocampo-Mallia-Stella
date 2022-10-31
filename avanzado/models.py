from django.db import models
from django.contrib.auth.models import User



class Moto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    chasis = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    contacto = models.IntegerField()
    
    
    def __str__(self):
        return f'Modelo: {self.modelo} - Marca: {self.marca} - Estado: {self.estado}'
    
    
    

class ExtensionMoto(models.Model):
    avatar = models.ImageField(upload_to='avatares',null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

