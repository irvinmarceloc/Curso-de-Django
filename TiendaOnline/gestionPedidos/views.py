from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["txtBuscar"]:
        #mensaje="Articulo buscado: %r" %request.GET["txtBuscar"]
        producto= request.GET["txtBuscar"]
        articulos = Articulos.objects.filter(nombre__icontains=producto)
        return render(request, "resultados_busqueda.html", {"articulos": articulos, "query":producto})
    else:
        mensaje="Campo vacío, no has introducido nada"
        return HttpResponse(mensaje)