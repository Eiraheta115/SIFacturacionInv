from .views import *
from django.urls import path

urlpatterns = [
    path('', inicio, name="inicio"),
    path('products', new_product, name="new_product")
]