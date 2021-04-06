from django.contrib import admin
from gestionPedidos.models import *
# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "tfno") #Para ver con formatos
    search_fields=("nombre","tfno") #Para filtrar por buscador

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    list_filter=("seccion",) #Para filtrar  por tipo

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    list_filter=("fecha",) #Interesante filtrar por fecha
    date_hierarchy="fecha" #Filtro como con formatos

admin.site.register(Clientes, ClientesAdmin) #Incluye en el panel, el segundo argumento agrega los filtros y formatos
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)