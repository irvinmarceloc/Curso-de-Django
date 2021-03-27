from django.http import HttpResponse
import datetime
from django.template import Template, Context
#A cada función dentro del archivo views se le denomina vistas 
def saludo(request): 
    doc_externo= open('/home/z49/Documentos/Curso Django/Prueba1/Prueba1/Plantillas/saludo.html')
    template = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    dom = template.render(ctx)
    return HttpResponse(dom)

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