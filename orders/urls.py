from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('crear/', views.orden_create, name='orden_create'),
]