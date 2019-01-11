from django import forms
from .models import *

class newBodegaForm(forms.ModelForm):
    class Meta:
        model = Bodegas
        fields = [
            'nombre',
            'descripcion',
        ]

