from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Producto
from cart.forms import CartAddProductForm


# Create your views here.
def index(request):
    return render(request, 'shop/producto/index.html')


def producto_lista(request, categoria_slug=None):

    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponible=True)
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        productos = productos.filter(categoria=categoria)
    return render(request,
                  'shop/producto/lista.html',
                  {'categoria': categoria,
                   'categorias': categorias,
                   'productos': productos})


def producto_detalle(request, id, slug):
    producto = get_object_or_404(Producto, id=id, slug=slug, disponible=True)
    cart_product_form = CartAddProductForm(producto=producto)
    return render(request,
                  'shop/producto/detalle.html',
                  {'producto': producto,
                   'cart_product_form': cart_product_form})