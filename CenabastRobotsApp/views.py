from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def proyectos(request):
    return render(request, "proyectos.html")

def gestioncontratos(request):
    return render(request, "gestioncontratos.html")

def usuarios(request):
    return render(request, "usuarios.html")

def finanzas(request):
    return render(request, "finanzas.html")

def facturacion(request):
    return render(request, "facturacion.html")

def personas(request):
    return render(request, "personas.html")



