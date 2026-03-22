from django.shortcuts import render, get_object_or_404
from . models import *

# Create your views here.

def accueil(request):
    articles = Article.objects.all()  
    return render(request, 'blog/accueil.html', context={'articles': articles})

def ajouter(request):
    return render(request, 'blog/ajouter_article.html')
       
def details(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/details.html', {'article': article})  