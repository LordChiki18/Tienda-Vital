from django.contrib import admin
from .models import Orden, OrdenItem

# Register your models here.

class OrdenItemInline(admin.TabularInline):
    model = OrdenItem
    raw_id_fields = ['producto']

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'email',
                    'direccion', 'codigo_postal', 'ciudad', 'pagado',
                    'creado', 'actualizado']
    list_filter = ['pagado', 'creado', 'actualizado']
    inlines = [OrdenItemInline]