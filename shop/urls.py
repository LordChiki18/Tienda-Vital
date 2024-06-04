from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.producto_lista, name='producto_lista'),
    path('productos/<slug:categoria_slug>/', views.producto_lista,
         name='producto_lista_por_categoria'),
    path('productos/<int:id>/<slug:slug>/', views.producto_detalle,
         name='producto_detalle'),
]