from django.db import models
from django.contrib.auth.models import User


# Initialisation de la class Categorie
class Categorie(models.Model):
    name = models.CharField(max_length=255, verbose_name="Non de la catégorie")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        
            
# Initialisation de la class Article
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auteur", verbose_name="Auteur")
    content = models.TextField(verbose_name="Contenu")
    date_of_publish = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")
    statut = models.BooleanField(default=False, verbose_name="Publié")
    category = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categorie")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        