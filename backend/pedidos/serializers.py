# pedidos/serializers.py

from rest_framework import serializers
from .models import Pedido, DetallePedido
from productos.models import Producto

# ---------------------------
# Serializer para el detalle del pedido (los ítems individuales)
# ---------------------------
class DetallePedidoSerializer(serializers.ModelSerializer):
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(), 
        source='producto',
        write_only=True # Solo se usa para escritura (POST/PUT), no se muestra en la respuesta
    )
    # Campo de solo lectura para mostrar el nombre del producto en la respuesta GET
    nombre_producto = serializers.CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = DetallePedido
        # Excluir 'pedido' aquí, ya que será gestionado por el Serializer padre (PedidoSerializer)
        fields = ('id', 'producto_id', 'nombre_producto', 'cantidad', 'precio_unidad')
        read_only_fields = ('precio_unidad',) # El precio se calcula en el backend

# ---------------------------
# Serializer principal para Pedidos (incluye los detalles anidados)
# ---------------------------
class PedidoSerializer(serializers.ModelSerializer):
    # Campo anidado para manejar una lista de DetallePedido
    detalles = DetallePedidoSerializer(many=True) 
    
    class Meta:
        model = Pedido
        fields = ('id', 'estado', 'fecha_creacion', 'total_pedido', 'detalles')
        read_only_fields = ('estado', 'total_pedido') # Estos campos son calculados por el backend