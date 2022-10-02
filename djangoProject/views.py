from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

from home.models import Persona

def crear_persona(request):
    persona1 = Persona(nombre='Juan' , apellido='Perez', edad=random.randrange(1,99), fecha_creacion=datetime.now())
    persona2 = Persona(nombre='Gastón', apellido='Galgo', edad=random.randrange(1,99), fecha_creacion=datetime.now())
    persona3 = Persona(nombre='Toph', apellido='Beifong', edad=random.randrange(1,99), fecha_creacion=datetime.now())
    persona1.save()
    persona2.save()
    persona3.save()#guarda a la persona creada en la DB, si esto no está, la persona no queda guardad.
    #no olvidar los save de cada objeto
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render()#sacar el diccionario si sacamos los parametros
    return HttpResponse(template_renderizado)

def ver_personas(request):
    personas = Persona.objects.all #trae todos los objetos de Persona que estén en la DB
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})
    return HttpResponse(template_renderizado)