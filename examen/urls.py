from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'), 
    path('Evento', views.listar_eventos, name='Evento'),
    path('Boletos', views.listar_boletos, name='Boletos'),
    path('producto', views.listar_producto, name='producto'),
]

