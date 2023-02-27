from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from .models import Reporter, Article

def create(request):
    rep = Reporter(first_name='Juanjo', last_name='Ruiz', email='juanjo@demo.com')
    rep.save()

    art1 = Article(headline='Se encuentra burro volador', pub_date=date(2022,5,5), reporter=rep)
    art1.save()

    art2 = Article(headline='El paro sube... otra vez', pub_date=date(2022,3,5), reporter=rep)
    art2.save()

    art3 = Article(headline='Político se roba a si mismo', pub_date=date(2022,8,5), reporter=rep)
    art3.save()

    #result = art1.reporter.first_name
    #result = rep.article_set.filter(headline='El paro sube... otra vez')
    result = rep.article_set.count()

    return HttpResponse(result)