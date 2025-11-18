# pedidos/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction, models
from .models import Pedido, DetallePedido
from .serializers import PedidoSerializer
from productos.models import Producto

class PedidoViewSet(viewsets.ModelViewSet):
    """
    ViewSet que maneja la creación y listado de pedidos.
    Sobrescribe el método 'create' para implementar la lógica transaccional.
    """
    queryset = Pedido.objects.all().order_by('-fecha_creacion')
    serializer_class = PedidoSerializer

    # Sobrescribimos la lógica de creación para manejar los detalles y el stock.
    def create(self, request, *args, **kwargs):
        # 1. Validar la estructura de datos
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 2. Iniciar la Transacción
        # Esto asegura que si una parte falla (ej: stock insuficiente), toda la operación 
        # (creación de Pedido, DetallePedido, y descuento de Stock) se revierte (rollback).
        with transaction.atomic():
            detalles_data = serializer.validated_data.pop('detalles')
            total_pedido = 0
            detalles_a_crear = []
            
            # Crear el objeto Pedido primero
            pedido = Pedido.objects.create(**serializer.validated_data)

            # 3. Procesar los Detalles (Validación de Stock y Cálculo de Total)
            for item_data in detalles_data:
                producto = item_data['producto']
                cantidad = item_data['cantidad']
                
                # a) Validación de Stock
                if producto.stock_actual < cantidad:
                    # Si el stock es insuficiente, se lanza una excepción que forzará el rollback de la transacción
                    return Response(
                        {"error": f"Stock insuficiente para {producto.nombre}. Disponible: {producto.stock_actual}"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                # b) Cálculo de Subtotal y Descuento de Stock
                precio_unidad = producto.precio
                subtotal = precio_unidad * cantidad
                total_pedido += subtotal

                # DESCUENTO DE STOCK (Lógica crucial)
                producto.stock_actual = models.F('stock_actual') - cantidad
                producto.save(update_fields=['stock_actual']) # Guardar el cambio de stock

                # c) Preparar el DetallePedido para la creación
                detalles_a_crear.append(DetallePedido(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unidad=precio_unidad
                ))

            # 4. Guardar los Detalles y Actualizar el Pedido Total
            DetallePedido.objects.bulk_create(detalles_a_crear)
            
            pedido.total_pedido = total_pedido
            pedido.save(update_fields=['total_pedido'])
        
        # 5. Respuesta Final (El pedido fue creado exitosamente)
        headers = self.get_success_headers(serializer.data)
        # Retornamos el pedido con todos los detalles
        return Response(PedidoSerializer(pedido).data, status=status.HTTP_201_CREATED, headers=headers)