from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Producto
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.

@require_POST
def cart_agregar(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.agregar(producto=producto,
                 cantidad=cd['cantidad'],
                 anular_cantidad=cd['anular'])
    return redirect('cart:cart_detalle')

@require_POST
def cart_remover(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    cart.remover(producto)
    return redirect('cart:cart_detalle')

def cart_detalle(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'cantidad': item['cantidad'],
            'anular': True})
    return render(request, 'cart/detalle.html', {'cart': cart})

