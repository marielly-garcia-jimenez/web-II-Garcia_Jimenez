from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def eventos(request):
    return render(request, 'examen/eventos.html')
