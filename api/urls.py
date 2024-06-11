from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api.views import CategoriaViews, ProductoViews, PersonaViews, PersonaUpdateView, OrdenViews, OrdenItemViews, \
    ValoracionViews

router = DefaultRouter()

router.register(r'Categoria', CategoriaViews)
router.register(r'Producto', ProductoViews)
router.register(r'Persona', PersonaViews)
router.register(r'Orden', OrdenViews)
router.register(r'OrdenItem', OrdenItemViews)
router.register(r'Valoracion', ValoracionViews)

urlpatterns = [
    path('gestion/', include(router.urls)),
    path('account/update', PersonaUpdateView.as_view(), name='actualizar-persona')
]
