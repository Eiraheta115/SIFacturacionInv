from .views import *
from django.urls import path

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear_producto', new_product, name="new_product"),
    path('crear_bodega', new_bodega, name="new_bodega"),
    path('crear_categoria', new_categoria, name="new_categoria"),
]