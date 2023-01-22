from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo ^_^")

def despedida(request):
    return HttpResponse("Adiós mundo cruel")