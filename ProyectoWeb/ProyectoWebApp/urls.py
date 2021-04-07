from django.conf.urls import url
from ProyectoWebApp import views

urlpatterns = [
    url(r'^home/', views.home, name="Home"),
    url(r'^servicios/', views.servicios, name="Servicios"),
    url(r'^tienda/', views.tienda, name="Tienda"),
    url(r'^blog/', views.blog, name="Blog"),
    url(r'^contacto/', views.contacto, name="Contacto"),
]


