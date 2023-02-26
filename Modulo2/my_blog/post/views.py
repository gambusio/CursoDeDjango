from django.shortcuts import render
from .models import Author, Entry

def queries(request):
    # Obtener todos los elementos
    authors = Author.objects.all()

    # Obtener los datos filtrados por condicion
    filtered = Author.objects.filter(email='victoria29@example.net')

    # Obtener un único objeto
    author = Author.objects.get(id=1)

    # Obtener los 10 primeros elementos
    limits = Author.objects.all()[:10]

    # Obtener 5 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    # Obtener todos los elementos ordenados por email
    orders = Author.objects.all().order_by('email')

    # Obtener todos los elementos cuyo ID sea menor o igual a 15
    filtered2 = Author.objects.filter(id__lte=15) 

    # Obtener todos los autores que contienen en su nombre la palabra yes
    filtered3 = Author.objects.filter(name__contains="yes")

    return render(request, 'post/queries.html', {
        'authors': authors, 
        'filtered': filtered, 
        'author': author, 
        'limits': limits, 
        'offsets': offsets,
        'orders': orders,
        'filtered2': filtered2,
        'filtered3': filtered3
    })