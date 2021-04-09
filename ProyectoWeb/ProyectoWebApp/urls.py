from django.conf.urls import url
from ProyectoWebApp import views

urlpatterns = [
    url(r'^home/', views.home, name="home"),
    url(r'^tienda/', views.tienda, name="tienda"),
    url(r'^blog/', views.blog, name="blog"),
    url(r'^contacto/', views.contacto, name="contacto"),
]


