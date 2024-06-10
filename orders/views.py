from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

from accounts.models import Persona
from shop.models import Producto
# Create your views here.

from .models import OrdenItem
from .forms import OrdenCreateForm
from cart.cart import Cart


def enviar_correo(to_email, subject, template_name, context):
    from_email = 'verdevital90@gmail.com'

    message = render_to_string(template_name, context)

    email = EmailMessage(subject, message, from_email, [to_email])
    email.content_subtype = "html"

    email.send(fail_silently=False)


def orden_create(request):
    cart = Cart(request)
    persona = Persona.objects.get(email=request.user.email)
    email = persona.email
    if request.method == 'POST':
        form = OrdenCreateForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.persona = persona
            orden.save()
            for item in cart:
                producto = item['producto']
                OrdenItem.objects.create(orden=orden,
                                         producto=item['producto'],
                                         precio=item['precio'],
                                         cantidad=item['cantidad'])
                producto.cantidad -= item['cantidad']
                producto.save()
            # limpiar el carrito
            cart.limpiar()

            total_cantidad = sum(item.cantidad for item in orden.items.all())
            total_costo = orden.get_total_costo()

            login_url = request.build_absolute_uri(reverse('shop:index'))

            subject = 'Resumen de compra'
            context = {
                'nombre': persona.nombre,
                'apellido': persona.apellido,
                'email': persona.email,
                'numero_documento': persona.numero_documento,
                'celular': persona.celular,
                'direccion': orden.direccion,
                'codigo_postal': orden.codigo_postal,
                'ciudad': orden.ciudad,
                'fecha': orden.creado,
                'total_cantidad': total_cantidad,
                'total_costo': total_costo,
                'login_url': login_url,
                'orden': orden,
            }

            enviar_correo(email, subject, 'ordenes/orden/resumen.html', context)

            return render(request,
                          'ordenes/orden/creado.html',
                          {'orden': orden})
    else:
        form = OrdenCreateForm()
    return render(request,
                  'ordenes/orden/crear.html',
                  {'cart': cart, 'form': form, 'persona': persona})
