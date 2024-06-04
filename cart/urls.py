from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detalle, name='cart_detalle'),
    path('agregar/<int:producto_id>/', views.cart_agregar, name='cart_agregar'),
    path('remover/<int:producto_id>/', views.cart_remover, name='cart_remover'),
]