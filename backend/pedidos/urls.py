from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet

# Registrar el ViewSet de Pedidos
router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    # Incluimos todas las rutas generadas por el router para pedidos
    path('', include(router.urls)),
]