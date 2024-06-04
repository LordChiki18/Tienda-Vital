from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api.views import CategoriaViews, ProductoViews

router = DefaultRouter()

router.register(r'Categoria', CategoriaViews)
router.register(r'Producto', ProductoViews)

urlpatterns = [
    path('gestion/', include(router.urls)),
]
