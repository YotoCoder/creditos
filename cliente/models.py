from django.db import models
# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        
        return f'{self.nombre}' 