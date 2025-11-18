# productos/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

# Crea un router para registrar automáticamente las rutas de los ViewSets
router = DefaultRouter()
# Registrar el ViewSet de Producto. Esto genera rutas como:
# /productos/ (GET: listar, POST: crear)
# /productos/{pk}/ (GET: detalle, PUT/PATCH: actualizar, DELETE: borrar)
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    # Incluimos todas las rutas generadas por el router
    path('', include(router.urls)),
]