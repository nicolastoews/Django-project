from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template

def hola(request):
    return HttpResponse('Django Project by Nikin')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La hora y fecha actual es {fecha_actual}')

def calcular_fecha_nac(request, edad):
    fecha = datetime.now().year - int(edad)
    return HttpResponse(f'Tu año de nacimiento aproximada para tus {edad} años sería: {fecha}')

def mi_template(request):
    cargar_archivo = open(r'C:\Projects\Python\Coder\Django-project\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)
