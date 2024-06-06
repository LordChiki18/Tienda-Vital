# from django import forms
#
# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
#
# class CartAddProductForm(forms.Form):
#     cantidad = forms.TypedChoiceField(
#                                 choices=PRODUCT_QUANTITY_CHOICES,
#                                 coerce=int)
#     anular = forms.BooleanField(required=False,
#                                   initial=False,
#                                   widget=forms.HiddenInput)

from django import forms
from shop.models import Producto


class CartAddProductForm(forms.Form):
    anular = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        producto = kwargs.pop('producto')  # Obtener el producto
        super(CartAddProductForm, self).__init__(*args, **kwargs)

        # Generar opciones de cantidad basadas en la cantidad disponible del producto
        self.fields['cantidad'] = forms.TypedChoiceField(
            choices=[(i, str(i)) for i in range(1, producto.cantidad + 1)],
            coerce=int
        )
