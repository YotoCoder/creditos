from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_400_BAD_REQUEST
from .models import Credito
from .serializers import CreditoSerializer

from producto.models import Producto
from cliente.models import Cliente

from django_filters.rest_framework import DjangoFilterBackend


class CreditoViewSet(viewsets.ModelViewSet):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer
    
    http_method_names = ['get', 'post']

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cliente', 'estado']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            cliente = Cliente.objects.get(id=request.data['cliente'])
            productos = request.data['producto']
            monto = 0
            for producto in productos:
                monto += Producto.objects.get(id=producto).precio
                # verificar si el producto esta en stock
                if Producto.objects.get(id=producto).stock == 0:
                    return Response({'error': 'No hay stock del producto'}, status=HTTP_400_BAD_REQUEST)
                else:
                    Producto.objects.filter(id=producto).update(stock=Producto.objects.get(id=producto).stock - 1)
            
            serializer.save(cliente=cliente, monto=monto, estado='Pendiente')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CancelCreditView(APIView):
    # cancelar credito y devolver el producto al stock
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer
    
    def patch(self, request, pk):
        credito = Credito.objects.get(id=pk)
        productos = credito.producto.all()
        for producto in productos:
            Producto.objects.filter(id=producto.id).update(stock=Producto.objects.get(id=producto.id).stock + 1)
        Credito.objects.filter(id=pk).update(estado='Cancelado')
        return Response({'message': 'Credito cancelado'}, status=status.HTTP_200_OK)

class PayCreditView(APIView):
    # pagar credito
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer
    
    def patch(self, request, pk):
        Credito.objects.filter(id=pk).update(estado='Pagado')
        return Response({'message': 'Credito pagado'}, status=status.HTTP_200_OK)