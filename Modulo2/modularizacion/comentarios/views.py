from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment

def test(request):
    return HttpResponse("Funciona ^_^!")

def create(request):
    # comment = Comment(name="Juan", score=5, comment="Todo genial perfectísimo")
    # comment.save()
    comment = Comment.objects.create(name="Alex")
    return HttpResponse("Vista para crear registros modelo comentario")

def delete(request):
    # comment = Comment.objects.get(id=1)
    # comment.delete()
    Comment.objects.filter(id=2).delete()
    return HttpResponse("Ruta para probar borrados")