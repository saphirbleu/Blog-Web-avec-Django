from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def accueil(request):
    articles = Article.objects.all()  
    return render(request, 'blog/accueil.html', context={'articles': articles})

@login_required
def ajouter(request):
    categories = Categorie.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        category_id = request.POST.get('category')
        new_category_name = request.POST.get('new_category', '').strip()

        category = None
        if new_category_name:
            category, _ = Categorie.objects.get_or_create(name=new_category_name)
        elif category_id:
            category = Categorie.objects.filter(id=category_id).first()

        if not title or not content:
            return render(request, 'blog/ajouter_article.html', {
                'error': 'Le titre et le contenu sont obligatoires.',
                'categories': categories,
                'title': title,
                'content': content,
                'selected_category': category_id,
                'new_category': new_category_name,
            })

        Article.objects.create(
            title=title,
            author=request.user,
            content=content,
            category=category,
            statut=True,
        )
        messages.success(request, 'Article créé avec succès.')
        return redirect('accueil')

    return render(request, 'blog/ajouter_article.html', {'categories': categories})
  
@login_required     
def details(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/details.html', {'article': article})  