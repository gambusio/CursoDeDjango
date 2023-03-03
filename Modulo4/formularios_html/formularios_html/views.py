from django.shortcuts import render
from django.http import HttpResponse

def form(request):
    return render(request, 'form.html', {})

def goal(request):
    if request.method != 'GET':
        return HttpResponse("El método no está soportado para esta ruta")
    
    name = request.GET['name']
    msg = request.GET['msg']
    return render(request, 'success.html', {'name': name, 'msg': msg})
    
    