from django.shortcuts import render
# Create your views here.

from .models import OrdenItem
from .forms import OrdenCreateForm
from cart.cart import Cart

def orden_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrdenCreateForm(request.POST)
        if form.is_valid():
            orden = form.save()
            for item in cart:
                OrdenItem.objects.create(orden=orden,
                                         producto=item['producto'],
                                         precio=item['precio'],
                                         cantidad=item['cantidad'])
            # limpiar el carrito
            cart.limpiar()
            return render(request, 
                      'ordenes/orden/creado.html',
                      {'orden': orden})
    else:
        form = OrdenCreateForm()
    return render(request,
                  'ordenes/orden/crear.html',
                  {'cart': cart, 'form': form})


