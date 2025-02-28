from django.db import models

class Localidad(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name 

class producto(models.Model):
    name = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    localidad_id = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Evento(models.Model):
    name = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    photo = models.URLField(default=1)
    fecha_inicio = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_fin = models.DateTimeField(auto_now_add=False, blank=True)
    localidad_id = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Boletos(models.Model):
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    tipo_boleto_id = models.IntegerField(default=1)
    photo = models.URLField(default=1)
    evento_id = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True)
    fecha = models.DateTimeField(auto_now_add=True, blank= True)  
