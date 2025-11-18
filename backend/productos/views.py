from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    Un ViewSet que provee automáticamente las acciones 'list', 'create', 
    'retrieve', 'update' y 'destroy'.
    
    Este ViewSet maneja todas las peticiones REST para los productos.
    """
    # Define qué datos obtener
    queryset = Producto.objects.all().order_by('nombre')
    
    # Define qué serializer usar para formatear los datos
    serializer_class = ProductoSerializer
    