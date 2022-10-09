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
from django.urls import path, include #include se agrega para vincular el archivo URLS de nuestra app a este urls

urlpatterns = [
    path('', include('home.urls')), # se agrega para vincular el archivo URLS de nuestra app a este urls. Se entiende como "Cuando no te ponga nada, vas a ir a home.urls"
    path('admin/', admin.site.urls),
    #migradas las URLS al archivo URLS dentro de HOME porque cada app deberia tener sus URLS allí.
]
