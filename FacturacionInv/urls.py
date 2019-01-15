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
    url(r'^new$', views.clientes_create, name='clientes_new'),
    url(r'^edit/(?P<pk>\d+)$', views.clientes_update, name='clientes_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.clientes_delete, name='clientes_delete'),
    url(r'^new$', views.proveedores_create, name='proveedores_new'),
    url(r'^edit/(?P<pk>\d+)$', views.proveedores_update, name='proveedores_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.proveedores_delete, name='proveedores_delete'),
]
