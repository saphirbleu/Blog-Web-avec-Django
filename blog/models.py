from django.db import models
from django.contrib.auth.models import User


# Initialisation de la class Categorie
class Categorie(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
# Initialisation de la class Article
class Article(models.Model):
    title = models.CharField(max_length=255)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    contain = models.TextField(max_length=400)
    date_of_publish = models.DateField(auto_now_add=True)
    statut = models.BooleanField()
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    