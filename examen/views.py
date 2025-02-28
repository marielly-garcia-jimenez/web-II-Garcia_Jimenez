from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render
from .models import Boletos, Evento, producto, Localidad
import json
def index(request):
    return HttpResponse("¡Hola desde la app examen!")

def principal(request):
    return render(request, 'examen/principal.html')
    
def eventos(request):
    return render(request, 'examen/eventos.html')


    