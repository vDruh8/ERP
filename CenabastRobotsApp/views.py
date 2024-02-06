from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def proyectos(request):
    return render(request, "proyectos.html")

def gestioncontratos(request):
    return render(request, "gestioncontratos.html")