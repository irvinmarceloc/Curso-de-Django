from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render 

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre 
        self.apellido = apellido
    

#A cada función dentro del archivo views se le denomina vistas 
def saludo(request): 

    persona1 = Persona("Nombre y ", "Apellido importado desde una clase")
    temas  = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    fecha_actual = datetime.datetime.now()
    return render(request, "saludo.html", {"nombre_persona": persona1.nombre, "apellido_persona": persona1.apellido, "fecha_hora_actual": fecha_actual, "temas": temas})

def despedida(request):
    return HttpResponse("Hasta luego mundo")

def fecha_hora(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"fecha.html", {"fecha_hora": fecha_actual})

def calcula_edad(request, agno, edad):
    
    edadActual = int(edad)
    tiempo = int(agno) - 2021
    edad = tiempo + edadActual
    dom="""<html>
            <body>
                <h3> En el año %s  tendras %s años </h3>
            </body>
        <html>""" %(agno ,edad)
    return HttpResponse(dom)

def CursoMint(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"CursoMint.html", {"fecha_hora": fecha_actual})