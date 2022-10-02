"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views #el punto indica que estamos importando desde la misma ubicación en la que está este archivo

urlpatterns = [
    path('hola/', views.hola),
    path('fecha/', views.fecha),
    path('fecha-nac/<int:edad>', views.calcular_fecha_nac), #<edad> es informacion que viene de la pag
    path('template/', views.mi_template),
    path('template/<str:nombre>', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('ver-personas/', views.ver_personas),
    path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),#sacar los arguemtnos de nombre y apellido si sacamos los arg en crear_persona
    path('admin/', admin.site.urls),
]
