from venv import create
from django.db import models
from producto.models import Producto
from cliente.models import Cliente

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Create your models here.

CHOICE_ESTADO = (
    ('Pendiente', 'Pendiente'),
    ('Cancelado', 'Cancelado'),
    ('Pagado', 'Pagado'),
)

class Credito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    productos = models.ManyToManyField(Producto)
    fecha = models.DateField()
    monto = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=100, choices=CHOICE_ESTADO, default='Pendiente')

    def __str__(self):
        return f'{self.cliente} - {self.monto}'

    class Meta:
        ordering = ['-fecha']