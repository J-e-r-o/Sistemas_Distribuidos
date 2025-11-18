from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Producto. 
    Convierte objetos Producto a JSON y viceversa.
    """
    class Meta:
        model = Producto
        # Usamos '__all__' para incluir todos los campos del modelo Producto.
        # Alternativamente, puedes listar los campos específicos:
        # fields = ['id', 'nombre', 'descripcion', 'precio', 'stock_actual', 'esta_disponible'] 
        fields = '__all__'