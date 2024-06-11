from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404

from accounts.forms import ValoracionForm
from accounts.models import Valoracion
from .models import Categoria, Producto


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
    valoraciones = Valoracion.objects.filter(producto=producto)
    mensaje = ''

    if request.method == 'POST':
        valoracion_form = ValoracionForm(request.POST)
        if valoracion_form.is_valid():
            try:
                nueva_valoracion = valoracion_form.save(commit=False)
                nueva_valoracion.producto = producto
                nueva_valoracion.usuario = request.user
                nueva_valoracion.save()
                mensaje = '¡Valoración guardada exitosamente!'
            except IntegrityError:
                mensaje = 'Ya has dejado una valoración para este producto.'
    else:
        valoracion_form = ValoracionForm()

    return render(request,
                  'shop/producto/detalle.html',
                  {'producto': producto,
                   'valoraciones': valoraciones,
                   'valoracion_form': valoracion_form,
                   'mensaje': mensaje})
