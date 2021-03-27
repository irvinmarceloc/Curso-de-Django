from django.http import HttpResponse
import datetime

#A cada función dentro del archivo views se le denomina vistas 
def saludo(request): 
    dom="""<html>
            <body>
                <h1> Hola mundo, mi primera pagina con Django  </h1>
            </body>
        <html>""" 
    return HttpResponse(dom)

#A cada función dentro del archivo views se le denomina vistas 
def despedida(request):
    return HttpResponse("Hasta luego mundo")

def fechaHora(request):
    fecha_actual = datetime.datetime.now()
    dom="""<html>
            <body>
                <h3> Fecha y hora actuales %s </h3>
            </body>
        <html>""" % fecha_actual
    return HttpResponse(dom)

def CalculaEdad(request, agno, edad):
    
    edadActual = int(edad)
    tiempo = int(agno) - 2021
    edad = tiempo + edadActual
    dom="""<html>
            <body>
                <h3> En el año %s  tendras %s años </h3>
            </body>
        <html>""" %(agno ,edad)
    return HttpResponse(dom)