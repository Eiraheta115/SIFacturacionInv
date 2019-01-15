from .views import *
from django.urls import path

urlpatterns = [
    path('', inicio, name="inicio"),
    path('nueva_venta', nueva_venta, name="nueva_venta"),
    path('nueva_compra', nueva_compra, name="nueva_compra"),
    path('busqueda', prueba, name="busqueda"),
]