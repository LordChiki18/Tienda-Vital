from django import forms
from .models import Orden

class OrdenCreateForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['nombre', 'apellido', 'email', 'direccion',
                  'codigo_postal', 'ciudad']