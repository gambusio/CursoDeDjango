from django.shortcuts import render

def optional(request, name='Dummy'):
    return render(request, 'optional.html', {'name': name})