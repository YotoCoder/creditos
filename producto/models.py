from django.db import models

from datetime import datetime

import os

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, blank=True) 
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.precio}'

    # colocarle la fecha en el nombre de la imagen
    def save(self, *args, **kwargs):
        self.imagen.name = f'{self.nombre}_{datetime.now().strftime("%d-%m-%Y")}{os.path.splitext(self.imagen.name)[1]}'
        super().save(*args, **kwargs)

