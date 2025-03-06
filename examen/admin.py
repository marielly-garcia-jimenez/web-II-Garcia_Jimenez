from django.contrib import admin
from .models import eventos, Localidad, boletos, productos

admin.site.register(eventos)

admin.site.register(Localidad)
admin.site.register(boletos)
admin.site.register(productos)