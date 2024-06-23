import secrets

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
import string

from django.template.loader import render_to_string
from django.urls import reverse

from accounts.forms import RegistroForm
from accounts.models import Persona


# Create your views here.
def generate_secure_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (
                len(password) >= 8 and  # Cumple con la longitud mínima
                any(char.isdigit() for char in password)  # Contiene al menos un carácter numérico
        ):
            return password


def enviar_correo(to_email, subject, template_name, context):
    from_email = 'verdevital90@gmail.com'

    message = render_to_string(template_name, context)

    email = EmailMessage(subject, message, from_email, [to_email])
    email.content_subtype = "html"

    email.send(fail_silently=False)


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            user = form.save(commit=False)  # No guardes el usuario en la base de datos todavía
            user.is_staff = False
            user.is_superuser = False
            generated_password = generate_secure_password()  # Genera una contraseña aleatoria
            user.set_password(generated_password)  # Configura la contraseña generada
            user.save()  # Ahora guarda el usuario en la base de datos
            # login(request, user)
            print("Usuario guardado en la base de datos")

            # Obtén los datos del usuario
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            email = form.cleaned_data.get('email')
            custom_username = user.custom_username

            home_url = request.build_absolute_uri(reverse('shop:index'))

            # Envía el correo electrónico
            subject = 'Registro exitoso'
            context = {
                'nombre': nombre,
                'apellido': apellido,
                'custom_username': custom_username,
                'generated_password': generated_password,
                'home_url': home_url,
            }

            enviar_correo(email, subject, 'accounts/registro_exitoso_email.html', context)

            return redirect('shop:index')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, custom_username=username, password=password)

        if user is not None and user.check_password(password):
            login(request, user)
            return JsonResponse({'success': True})  # Envía una respuesta JSON indicando éxito

        else:
            error_message = "Usuario o contraseña incorrectos"
            return JsonResponse({'success': False, 'error_message': error_message},
                                status=400)  # Envía un mensaje de error en JSON y establece el código de estado HTTP a 400 (Bad Request)

    return render(request, 'accounts/login.html')


def cerrar_sesion(request):
    logout(request)  # Cierra la sesión del usuario actual
    return redirect('shop:index')  # Redirige al usuario a la página de inicio u otra página de tu elección


@login_required
def mis_datos(request):
    try:
        persona = Persona.objects.get(email=request.user.email)
    except Persona.DoesNotExist:
        persona = None

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        context = {
            'persona': persona
        }
        return render(request, 'accounts/actualizar_cuenta.html', context)

    # Si no es una solicitud AJAX, renderiza una plantilla general (opcional)
    return render(request, 'accounts/resumen.html', {'persona': persona})
