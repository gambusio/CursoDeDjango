from django.shortcuts import render 

def info(request):
    return render(request, 'info.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})