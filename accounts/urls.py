from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [

    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('registro/', views.registro_usuario, name='registro'),
    path('datos/', views.mis_datos, name='datos'),

]
