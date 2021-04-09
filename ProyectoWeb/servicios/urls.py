from django.conf.urls import url
from servicios import views

urlpatterns = [    
    url('', views.servicios, name="servicios"),
]