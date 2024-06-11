from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from shop.models import Producto


class PersonaManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo "email" es obligatorio.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Persona(AbstractBaseUser, PermissionsMixin):
    persona_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_documento = models.CharField(max_length=255, unique=True)
    celular = models.CharField(max_length=255)
    custom_username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    objects = PersonaManager()

    USERNAME_FIELD = 'custom_username'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'numero_documento','email']

    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.custom_username:
            # Genera el username a partir de la primera letra del nombre y número de documento
            self.custom_username = f"{self.nombre[0]}{self.numero_documento}"
        super().save(*args, **kwargs)


class Valoracion(models.Model):
    usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'producto')