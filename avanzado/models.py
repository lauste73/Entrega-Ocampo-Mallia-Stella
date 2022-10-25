from django.db import models



class Moto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    chasis = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    contacto = models.IntegerField()
    
    def __str__(self):
        return f'Modelo: {self.modelo} - Marca: {self.marca} - Chasis: {self.chasis}'

