from django import forms

from accounts.models import Persona


class RegistroForm(forms.ModelForm):
    nombre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    apellido = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    numero_documento = forms.CharField(max_length=255,
                                       widget=forms.TextInput(attrs={'placeholder': 'Nro. De Documento'}))
    direccion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Dirección'}))
    celular = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Celular'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = Persona
        fields = (
            'nombre', 'apellido', 'numero_documento', 'direccion', 'celular', 'email')
