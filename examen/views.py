from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.shortcuts import render
from .models import boletos, eventos, productos, Localidad
import json
from django.http import JsonResponse
from datetime import datetime

def principal(request):
    return render(request, 'examen/principal.html')

def listar_eventos(request):  
    evento = eventos.objects.all()  
    return render(request, 'examen/eventos.html', {"eventos": evento})

def listar_boletos(request):
    boleto = boletos.objects.all()
    return render(request, 'examen/boletos.html', {"boletos": boleto})

def listar_boletos_eventos(request, id):
    boleto = boletos.objects.filter(evento_id__id = id)
    return render(request, 'examen/boletos.html', {"boletos": boleto})

def listar_producto(request):
    productos_data = productos.objects.all()
    return render(request, 'examen/producto.html', {"productos": productos_data})

def obtener_boletos(request, evento_id):
    boletos = Boleto.objects.filter(evento_id=evento_id)
    if not boletos.exists():
        return JsonResponse({'message': 'Sin productos disponibles'}, status=404)

    return JsonResponse(list(boletos.values()), safe=False)

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(body)
        if form.is_valid():
            form.save()
            return redirect('producto') 
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})


def agregar_evento(request):
    localidades = Localidad.objects.all()
    return render(request, 'examen/agregar_evento.html', {'localidades': localidades})


def validar_agregarEvento(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)


        nombre = body.get('name')
        fecha_inicio_str = body.get('fecha_inicio')
        fecha_fin_str = body.get('fecha_fin')
        localidad_id = body.get('localidad_id')
        print (nombre)
       
        if not nombre or not fecha_inicio_str or not fecha_fin_str or not localidad_id:
            return JsonResponse({'success': False, 'message': 'Todos los campos son requeridos.'}, status=400)

        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%dT%H:%M')
            fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%dT%H:%M')
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Formato de fecha inválido.'}, status=400)

        if fecha_inicio < datetime.now():
            return JsonResponse({'success': False, 'message': 'La fecha de inicio debe ser mayor al día de hoy.'}, status=400)

        if fecha_fin < fecha_inicio:
            return JsonResponse({'success': False, 'message': 'La fecha de fin no puede ser menor que la fecha de inicio.'}, status=400)

        
        ultimo_evento = eventos.objects.order_by('-id').first()  
        if ultimo_evento and ultimo_evento.localidad_id_id == localidad_id:
            return JsonResponse({'success': False, 'message': 'No puedes agregar dos eventos seguidos de la misma localidad.'}, status=400)

        
        localidad = get_object_or_404(Localidad, id=localidad_id)

        evento = eventos(
            name=nombre,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            localidad_id=localidad
        )

        evento.save()

        return JsonResponse({
            'success': True,
            'evento': {
                'id': evento.id,
                'nombre': evento.name,
                'fecha_inicio': str(evento.fecha_inicio),
                'fecha_fin': str(evento.fecha_fin),
                'localidad': evento.localidad_id_id,
            },
            'message': "Se creo el evento"
        },status=201)

    return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=400)


def validar_eliminarEvento(request):

    body = json.loads(request.body.decode('utf-8'))
    evento_id = body.get("id")

    evento = get_object_or_404(eventos, id=evento_id)
    if not evento: 
      return JsonResponse({"message": "no se elimino el evento", "status": "success"}, status=500)
    evento.delete()

    return JsonResponse({"message": "Evento eliminado", "status": "success"}, status=200)





    