from django.db import models
from shop.models import Producto

class Orden(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=250)
    codigo_postal = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    pagado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-creado']
        indexes = [
            models.Index(fields=['-creado']),
            ]
        verbose_name = 'orden'
        verbose_name_plural = 'órdenes'

    def __str__(self):
        return f'Orden {self.id}'
    
    def get_total_costo(self):
        return sum(item.get_costo() for item in self.items.all())

class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden,
                              related_name='items',
                              on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,
                                related_name='orden_items',
                                on_delete=models.CASCADE)
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)

    def get_costo(self):
        return self.precio * self.cantidad