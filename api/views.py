from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated

from accounts.models import Persona, Cliente
from api.serializers import CategoriaSerializer, ProductoSerializer, PersonaSerializer, ClienteSerializer, \
    PersonaUpdateSerializer
from shop.models import Categoria, Producto


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
        return Persona.objects.get(custom_username=self.request.user)

    def perform_update(self, serializer):
        # Realiza la actualización de la persona
        serializer.save()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ClienteViews(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ClienteSerializer
