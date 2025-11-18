"""
URL configuration for ki_um_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# ki_um_core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas para nuestra API REST
    # Todos los endpoints de Productos se servirán bajo el prefijo 'api/v1/'
    path('api/v1/', include('productos.urls')),
    path('api/v1/', include('pedidos.urls')),  
    # Aquí podríamos agregar más rutas en el futuro, ej: path('api/v1/', include('pedidos.urls')),
]