from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('crear/', views.orden_create, name='orden_create'),
    path('resumen-pedidos/', views.resumen_ordenes, name='resumen_ordenes'),
    path('orden/<int:orden_id>', views.detalle_orden, name='detalle_orden')
]
