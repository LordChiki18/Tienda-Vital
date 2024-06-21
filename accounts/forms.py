from django import forms

from accounts.models import Persona, Valoracion


class RegistroForm(forms.ModelForm):
    nombre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    apellido = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    numero_documento = forms.CharField(max_length=255,
                                       widget=forms.TextInput(attrs={'placeholder': 'Nro. De Documento'}))
    celular = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Celular'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = Persona
        fields = (
            'nombre', 'apellido', 'numero_documento', 'celular', 'email')


class ValoracionForm(forms.ModelForm):
    PUNTUACION_CHOICES = [
        (1, '1 estrella'),
        (2, '2 estrellas'),
        (3, '3 estrellas'),
        (4, '4 estrellas'),
        (5, '5 estrellas'),
    ]
    puntuacion = forms.TypedChoiceField(choices=PUNTUACION_CHOICES, coerce=int)
    comentario = forms.CharField(max_length=255, widget=forms.Textarea(attrs=({'placeholder': 'Comentario'})))

    class Meta:
        model = Valoracion
        fields = ['puntuacion', 'comentario']
