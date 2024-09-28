from django.urls import path
from .views import (
    producto_list, producto_create, producto_update, producto_delete,
    cliente_list, cliente_create, cliente_update, cliente_delete,
    venta_list, venta_create, venta_update, venta_delete
)

urlpatterns = [
    path('productos/', producto_list, name='producto_list'),
    path('productos/crear/', producto_create, name='producto_create'),
    path('productos/editar/<int:pk>/', producto_update, name='producto_update'),
    path('productos/eliminar/<int:pk>/', producto_delete, name='producto_delete'),
    
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/crear/', cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', cliente_update, name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', cliente_delete, name='cliente_delete'),

    path('ventas/', venta_list, name='venta_list'),
    path('ventas/crear/', venta_create, name='venta_create'),
    path('ventas/editar/<int:pk>/', venta_update, name='venta_update'),
    path('ventas/eliminar/<int:pk>/', venta_delete, name='venta_delete'),
]
