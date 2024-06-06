from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from accounts.models import Persona
from shop.models import Categoria, Producto


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
        fields = ['email', 'ciudad_id', 'nombre', 'apellido', 'direccion',
                  'celular']


# class ClienteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cliente
#         fields = '__all__'
