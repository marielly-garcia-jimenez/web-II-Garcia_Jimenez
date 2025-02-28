from django.contrib import admin
from .models import Evento, Localidad, Boletos, producto

admin.site.register(Evento)

admin.site.register(Localidad)
admin.site.register(Boletos)
admin.site.register(producto)