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

    persona1 = Persona("Felipe", "Lopez")
    temas  = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    #nombre = "Juan"
    #apellido = "Perez" 
    fecha_actual = datetime.datetime.now()
    #doc_externo= open('/home/z49/Documentos/Curso Django/Prueba1/Prueba1/Plantillas/saludo.html')
    
    #doc_externo = loader.get_template('saludo.html')


    #template = Template(doc_externo.read())
    #Context({"nombre_persona": persona1.nombre, "apellido_persona": persona1.apellido, "fecha_hora_actual": fecha_actual, "temas": temas})
    #ctx = {"nombre_persona": persona1.nombre, "apellido_persona": persona1.apellido, "fecha_hora_actual": fecha_actual, "temas": temas}
    #dom = doc_externo.render(ctx)
    #return HttpResponse(dom)
    return render(request, "saludo.html", {"nombre_persona": persona1.nombre, "apellido_persona": persona1.apellido, "fecha_hora_actual": fecha_actual, "temas": temas})


#A cada función dentro del archivo views se le denomina vistas 
def despedida(request):
    return HttpResponse("Hasta luego mundo")

def fecha_hora(request):
    fecha_actual = datetime.datetime.now()
    dom="""<html>
            <body>
                <h3> Fecha y hora actuales %s </h3>
            </body>
        <html>""" % fecha_actual
    return HttpResponse(dom)

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

def CursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"CursoC.html", {"fecha_hora": fecha_actual})