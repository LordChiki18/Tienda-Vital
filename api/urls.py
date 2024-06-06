from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api.views import CategoriaViews, ProductoViews, PersonaViews, PersonaUpdateView

router = DefaultRouter()

router.register(r'Categoria', CategoriaViews)
router.register(r'Producto', ProductoViews)
router.register(r'Persona', PersonaViews)

urlpatterns = [
    path('gestion/', include(router.urls)),
    path('account/update', PersonaUpdateView.as_view(), name='actualizar-persona')
]
