from django.contrib import admin

from . models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date_of_publish', 'statut', 'content')
    ordering = ['-date_of_publish']

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)