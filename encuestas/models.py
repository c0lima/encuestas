from django.db import models
import datetime
from django.utils import timezone


class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    fecha_pub = models.DateField('Fecha publicada')

    def publicada_recientemente(self):
        return self.fecha_pub >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.pregunta_texto

class Eleccion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    eleccion_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)


    def __str__(self):
        return self.eleccion_texto
# Create your models here.
