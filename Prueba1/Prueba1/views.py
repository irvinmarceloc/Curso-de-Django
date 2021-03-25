from django.http import HttpResponse

#A cada función dentro del archivo views se le denomina vistas 
def saludo(request): 
    return HttpResponse("Hola mundo, mi primera pagina con Django")

#A cada función dentro del archivo views se le denomina vistas 
def despedida(request):
    return HttpResponse("Hasta luego mundo")