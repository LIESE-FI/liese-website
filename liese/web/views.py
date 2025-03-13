from django.shortcuts import render

def index(request):
    integrantes = [
        {"nombre": "Rubi Janet Núñez Dorantes", "rol": "Tesista de maestría", "descripcion": "Contribuye al diseño de sistemas de comando y control."},
        {"nombre": "Nombre Apellido", "rol": "Investigador", "descripcion": "Desarrollo de instrumentación para sistemas embebidos."},
    ]
    return render(request, "web/index.html", {"integrantes": integrantes})

