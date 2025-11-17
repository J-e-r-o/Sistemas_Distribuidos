from django.db import models
from productos.models import Producto # <-- Importamos el modelo de la otra aplicación

class Pedido(models.Model):
    """Representa el pedido completo realizado por el cliente."""
    ESTADOS = (
        ('RECIBIDO', 'Recibido'),
        ('EN_PREPARACION', 'En Preparación'),
        ('LISTO_RETIRAR', 'Listo para Retirar'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    )
    
    # Podrías agregar un campo para el usuario cuando definamos el modelo 'Usuario'
    # usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Cliente") 
    
    estado = models.CharField(max_length=20, choices=ESTADOS, default='RECIBIDO', verbose_name="Estado del Pedido")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora del Pedido")
    
    # Campo para almacenar el costo total del pedido.
    total_pedido = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, verbose_name="Costo Total")

    class Meta:
        verbose_name = "Pedido de Cliente"
        verbose_name_plural = "Pedidos de Clientes"
        ordering = ['-fecha_creacion'] # Los pedidos más nuevos primero

    def __str__(self):
        return f"Pedido #{self.id} - Estado: {self.estado}"

class DetallePedido(models.Model):
    """Guarda los productos individuales dentro de un Pedido."""
    
    # Relación con el Pedido (Muchos detalles apuntan a un Pedido)
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    
    # Relación con el Producto (Muchos detalles apuntan a un Producto)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT) # PROTECT: evita que se borre un Producto si hay pedidos que lo referencian.
    
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad Solicitada")
    
    # Almacenamos el precio de la unidad al momento de la compra (para evitar inconsistencias si el precio cambia después).
    precio_unidad = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio en el momento del Pedido")

    class Meta:
        verbose_name = "Detalle de Pedido"
        verbose_name_plural = "Detalles de Pedidos"
        # Restricción: No se puede repetir el mismo producto en el mismo pedido.
        unique_together = ('pedido', 'producto') 

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre}"