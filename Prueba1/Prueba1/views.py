from django.http import HttpResponse

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

