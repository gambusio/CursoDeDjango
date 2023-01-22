from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo ^_^")

def despedida(request):
    return HttpResponse("Adiós mundo cruel")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("No eres mayor de edad")