from django.shortcuts import render, HttpResponse

# Create your views here.

def update(data):
    return HttpResponse("UPDATE - Hola Mundo! Team 5, Codo a Codo 4.0")

def create(data):
    return HttpResponse("CREATE - Hola Mundo! Team 5, Codo a Codo 4.0")

def delete(data):
    return HttpResponse("DELETE - Hola Mundo! Team 5, Codo a Codo 4.0")

def read(data):
    return HttpResponse("READ - Hola Mundo! Team 5, Codo a Codo 4.0")

def home(request):
    miRespuesta = HttpResponse("Hola Mundo! Team 5, Codo a Codo 4.0")

    if request.method == "GET":
        miRespuesta = read(request)
    elif request.method == "PUT":
        miRespuesta = update(request)
    elif request.method == "DELETE":
        miRespuesta = delete(request)
    else: # Que method es?POST
        miRespuesta = create(request)

    return miRespuesta
    
def victorCreado(request):
    return HttpResponse("Hola soy victor")

def valenPage(request):
    return HttpResponse("Hola, soy la pagina web de Valentina") 

def diego(request):
    return HttpResponse("Hola soy Diego Barale del team 5")   

