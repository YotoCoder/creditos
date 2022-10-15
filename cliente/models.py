from django.db import models


from django.db.models.signals import pre_save, post_save, pre_delete, post_delete

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        print('metodo save')
        print('self.nombre: ', self.nombre)
        print('args: ', args)
        print('kwargs: ', kwargs)


        super(Cliente, self).save(*args, **kwargs)


def pre_save_cliente(sender, instance, *args, **kwargs):
    print('Se va a guardar un Cliente [antes de guardar]')
    print('instance.nombre: ', instance.nombre)


def post_save_cliente(sender, instance, created, *args, **kwargs):
    print('Se ha guardado un Cliente [despues de guardar]')
    print('instance.nombre: ', instance.nombre)
    print('created: ', created)

    if created:
        print('Se ha creado un Cliente')
    else:
        print('Se ha actualizado un Cliente')


def pre_delete_cliente(sender, instance, *args, **kwargs):
    print('Se va a eliminar un Cliente')

def post_delete_cliente(sender, instance, *args, **kwargs):
    print('Se ha eliminado un Cliente')

pre_save.connect(pre_save_cliente, sender=Cliente)
post_save.connect(post_save_cliente, sender=Cliente)
    
pre_delete.connect(pre_delete_cliente, sender=Cliente)
post_delete.connect(post_delete_cliente, sender=Cliente)