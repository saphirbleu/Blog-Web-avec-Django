from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>/', views.details, name='details'),
    path('ajouter/', views.ajouter, name='ajouter'),
    
]
