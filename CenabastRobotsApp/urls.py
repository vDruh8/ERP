from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('gestioncontratos/', views.gestioncontratos, name='gestioncontratos'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('finanzas/', views.finanzas, name='finanzas'),
    path('facturacion/', views.facturacion, name='facturacion'),
]


