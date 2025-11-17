from django.db import models

class Producto(models.Model):
    # Clave primaria autoincremental de Django (automática)
    # id = models.AutoField(primary_key=True) 

    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Producto")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    
    # Stock y Precio
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio Unitario")
    stock_actual = models.IntegerField(default=0, verbose_name="Stock Disponible")
    
    # Estado (activo/inactivo para la venta)
    esta_disponible = models.BooleanField(default=True, verbose_name="Disponible para Venta")
    
    # Fechas de registro
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto de Cantina"
        verbose_name_plural = "Productos de Cantina"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre