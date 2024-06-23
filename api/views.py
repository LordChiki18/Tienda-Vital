from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated

from accounts.models import Persona, Valoracion
from api.serializers import CategoriaSerializer, ProductoSerializer, PersonaSerializer, PersonaUpdateSerializer, \
    OrdenSerializer, OrdenItemSerializer, ValoracionSerializer, ProveedorSerializer
from orders.models import Orden, OrdenItem
from shop.models import Categoria, Producto, Proveedor


# Create your views here.

class CategoriaViews(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategoriaSerializer


class ProductoViews(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductoSerializer


class PersonaViews(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PersonaSerializer


class PersonaUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PersonaUpdateSerializer

    def get_object(self):
        # Recupera la persona asociada al usuario autenticado
        try:
            return Persona.objects.get(email=self.request.user.email)
        except Persona.DoesNotExist:
            raise Http404("Persona matching query does not exist.")

    def perform_update(self, serializer):
        # Realiza la actualización de la persona
        serializer.save()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class OrdenViews(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrdenSerializer


class OrdenItemViews(viewsets.ModelViewSet):
    queryset = OrdenItem.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrdenItemSerializer


class ValoracionViews(viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ValoracionSerializer


class ProveedorViews(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProveedorSerializer
