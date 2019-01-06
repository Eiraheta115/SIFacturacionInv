from django import forms

from .models import Clientes
from .models import Proveedores

class ClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ('idcliente', 'codigocli', 'registro', 'telefono', 'email', 'nombre', 'direccion', 'dui', 'saldo')

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ('idproveedor', 'codigoprov', 'registro', 'telefono', 'email', 'nombre', 'direccion', 'dui', 'saldo')
