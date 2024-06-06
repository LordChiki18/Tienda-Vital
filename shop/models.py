from django.db import models
from django.urls import reverse


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['nombre']
        indexes = [models.Index(fields=['nombre']), ]
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('shop:producto_lista_por_categoria',
                       args=[self.slug])


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d', blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField(default=0)  # Nuevo campo cantidad
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['nombre']),
            models.Index(fields=['-creado']),
        ]

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.cantidad == 0:
            self.disponible = False
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:producto_detalle',
                       args=[self.id, self.slug])
