from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContactForm

def form(request):
    comment_form = CommentForm({'name': 'Juanjo', 'url': 'https://cristina.media', 'comment': 'Libros y más'})
    return render(request, 'form.html', {'comment_form': comment_form})

def goal(request):
    if request.method != 'POST':
        return HttpResponse("Método no permitido")
    name = request.POST['name']
    return HttpResponse(name)

def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Acciones cuando los datos son correctos
            return HttpResponse("Valido")
        else:
            # Acciones cuando los datos no son válidos
            return render(request, 'widget.html', {'form': form})
