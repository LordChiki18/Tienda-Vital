from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from accounts.models import Persona, Valoracion
from shop.models import Categoria, Producto
from orders.models import Orden, OrdenItem


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

    def create(self, validated_data):
        # Hashea la contraseña antes de guardarla
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)


class PersonaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['email', 'nombre', 'apellido', 'celular']


class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'


class OrdenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenItem
        fields = '__all__'


class ValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = '__all__'
