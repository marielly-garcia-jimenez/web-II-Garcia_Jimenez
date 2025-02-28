from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render
from .models import Boletos, Evento, producto, Localidad
import json

def principal(request):
    return render(request, 'examen/principal.html')

def listar_eventos(request):  
    eventos = Evento.objects.all()  
    return render(request, 'examen/eventos.html', {"eventos": eventos})

def listar_boletos(request):
    boletos = Boletos.objects.all()
    return render(request, 'examen/boletos.html', {"boletos": boletos})

def listar_producto(request):
    productos_data = producto.objects.all()
    return render(request, 'examen/producto.html', {"productos": productos_data})



    