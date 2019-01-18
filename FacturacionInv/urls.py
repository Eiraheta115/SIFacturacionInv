from .views import *
from django.urls import path
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('', inicio, name="inicio"),
    path('nueva_venta', nueva_venta, name="nueva_venta"),
    path('nueva_compra', nueva_compra, name="nueva_compra"),
    path('busqueda', prueba, name="busqueda"),
    path('crear_producto', new_product, name="new_product"),
    path('crear_bodega', new_bodega, name="new_bodega"),
    path('crear_categoria', new_categoria, name="new_categoria"),
    path('products', new_product, name="new_product"),
    path('listar_bodega', BodegasList.as_view(), name="list_bodega"),
    path('listar_categoria', CategoriasList.as_view(), name="list_categoria"),
    path('listar_producto', ProductosList.as_view(), name="list_categoria"),
    path('nuevo_cliente', clientes_create, name='clientes_new'),
    path('editar_cliente', clientes_update, name='clientes_edit'),
    path('eliminar_cliente', clientes_delete, name='clientes_delete'),
    path('nuevo_proveedor', proveedores_create, name='proveedores_new'),
    path('editar_proveedor', proveedores_update, name='proveedores_edit'),
    path('eliminar_proveedor', proveedores_delete, name='proveedores_delete'),
    path('reporte_ventas', reporte_ventas, name='reporte_ventas'),
    url(r'^getVentas$', getVentas, name='getVentas'),
]
