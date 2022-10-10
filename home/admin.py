from django.contrib import admin
from home.models import Persona

# Register your models here.
admin.site.register(Persona) #Necesitamos poner esto para que podamos manejar desde el sector ADMIN de Django todo lo de Persona
#Se debe agregar la linea de arriba por cada modelo que tenga nuestro proyecto
