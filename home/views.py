from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect #new import
import random
from home.forms import BusquedaPersona, PersonaFormulario

from home.models import Persona

def hola(request):
    return HttpResponse('<h1>Django Project by Nikin</h1>')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La hora y fecha actual es {fecha_actual}')

def calcular_fecha_nac(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu año de nacimiento aproximada para tus {edad} años sería: {fecha}')

def mi_template(request):
    cargar_archivo = open(r'C:\Projects\Python\Coder\Django-project\home\templates\mi_template.html', 'r')#Puede generar error por lo que se cambió en linea 57 de settings.py donde le indicamos que busque los templates desde el directorio base.
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    template = loader.get_template('home/tu_template.html')
    template_renderizado = template.render({'persona': nombre})
    return HttpResponse(template_renderizado)

def prueba_template(request):
    mi_contexto = {
        'rango': list(range(1,11)),
        'valor_random': random.randrange(1,11)
    }
    template = loader.get_template('home/prueba_template.html')
    template_renderizado = template.render(mi_contexto)
    return HttpResponse(template_renderizado)

def crear_persona(request):
    if request.method == 'POST':
        formulario = PersonaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_creacion = data.get('fecha_creacion', datetime.now()) #lo crea vacio no se por que
            
            persona = Persona(nombre=nombre, apellido=apellido, edad=random.edad, fecha_creacion=fecha_creacion)
            persona.save() #guarda a la persona creada en la DB, si esto no está, la persona no queda guardad.
                            #no olvidar los save de cada objeto
            # return render(request,'home/ver_persona.html', {}) #Este te trae solo los datos que acabas de ingresar
            return redirect('ver_personas') #este te manda directamente a ver_personas mostrando todos los datos
    formulario = PersonaFormulario()
    return render(request,'home/crear_persona.html', {'formulario': formulario}) #new, reemplaza las 3 lineas de arriba

def ver_personas(request):
    nombre = request.GET.get('nombre')
    if nombre:
        personas = Persona.objects.filter(nombre__icontains = nombre)
    else:
        personas = Persona.objects.all() #trae todos los objetos de Persona que estén en la DB
    formulario = BusquedaPersona()
    return render(request, 'home/ver_personas.html', {'personas': personas, 'formulario': formulario}) #new, reemplaza las 3 lineas de arriba

def index(request):
    return render(request, 'home/index.html')