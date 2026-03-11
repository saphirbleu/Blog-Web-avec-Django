from django.contrib import admin

from . models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'auth', 'contain', 'date_of_publish', 'statut', 'category']

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)