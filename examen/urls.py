from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('eventos/', views.listar_eventos, name='eventos'),
    path('boletos/', views.listar_boletos, name='boletos'),
    path('boletos/<int:id>', views.listar_boletos_eventos, name='boletos_eventos'),
    path('productos/', views.listar_producto, name='productos'),
    path('agregar_evento/', views.agregar_evento, name='agregar_evento'),
    path('validar_agregar_evento/', views.validar_agregarEvento, name='validar_agregarevento'),
    path('validar_eliminar_evento/', views.validar_eliminarEvento, name='validar_eliminarevento'),
]

