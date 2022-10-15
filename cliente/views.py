from rest_framework import viewsets

from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    # filtrar por nombre que empieza con 
    def get_queryset(self):
        queryset = Cliente.objects.all()
        nombre = self.request.query_params.get('nombre', None)
        if nombre is not None:
            queryset = queryset.filter(nombre__startswith=nombre)
        return queryset