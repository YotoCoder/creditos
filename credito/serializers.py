from rest_framework import serializers
from .models import Credito
from cliente.models import Cliente
from producto.models import Producto 

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'dni', 'telefono')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CreditoSerializer(serializers.ModelSerializer):
    
    # # mostrar todos los datos del cliente
    # cliente = ClienteSerializer(
    #     many=False,
    #     read_only=True
    # )

    # # mostrar todos los datos del producto
    # productos = ProductoSerializer(
    #     many=True
    # )

    class Meta:
        model = Credito
        fields = '__all__'