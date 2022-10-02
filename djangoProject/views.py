from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

from home.models import Persona

def hola(request):
    return HttpResponse('Django Project by Nikin')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La hora y fecha actual es {fecha_actual}')

def calcular_fecha_nac(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu año de nacimiento aproximada para tus {edad} años sería: {fecha}')

def mi_template(request):
    cargar_archivo = open(r'C:\Projects\Python\Coder\Django-project\templates\mi_template.html', 'r')#Puede generar error por lo que se cambió en linea 57 de settings.py donde le indicamos que busque los templates desde el directorio base.
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})
    return HttpResponse(template_renderizado)

def prueba_template(request):
    mi_contexto = {
        'rango': list(range(1,11)),
        'valor_random': random.randrange(1,11)
    }
    template = loader.get_template('prueba_template.html')
    template_renderizado = template.render(mi_contexto)
    return HttpResponse(template_renderizado)

def crear_persona(request, nombre, apellido):#sacar param nom y apell
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    #copair la linea de arriba 3 veces para crear a los 3 familiares (persona 1, 2 y 3)
    persona.save() #guarda a la persona creada en la DB, si esto no está, la persona no queda guardad.
    #no olvidar los save de cada objeto
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'persona': persona})#sacar el diccionario si sacamos los parametros
    return HttpResponse(template_renderizado)

def ver_personas(request):
    personas = Persona.objects.all #trae todos los objetos de Persona que estén en la DB
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})
    return HttpResponse(template_renderizado)