from django.db import models

from producto.models import Producto

from cliente.models import Cliente


# Create your models here.

CHOICE_ESTADO = (
    ('Pendiente', 'Pendiente'),
    ('Cancelado', 'Cancelado'),
    ('Vencido', 'Vencido'),
)

class Credito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    producto = models.ManyToManyField(Producto)
    fecha = models.DateField()
    monto = models.FloatField()
    estado = models.CharField(max_length=100, choices=CHOICE_ESTADO, default='Pendiente')

    def __str__(self):
        return self.cliente.nombre
