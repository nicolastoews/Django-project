from unittest.util import _MAX_LENGTH
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateTimeField(null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}' #para que en django admin nos aparezca cada objeto con el nombre y apellido de la persona que es dicho objeto
