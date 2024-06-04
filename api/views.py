from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import CategoriaSerializer, ProductoSerializer
from shop.models import Categoria, Producto


# Create your views here.

class CategoriaViews(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoViews(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
