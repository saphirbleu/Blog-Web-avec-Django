# Blog Web avec Django

## Description

Ce projet consiste à développer une application web de type **blog**
permettant de publier et consulter des articles.

L'application est développée avec le framework **Django** et utilise
**Bootstrap** pour l'interface utilisateur.

Le blog permet : - la publication d'articles - la classification des
articles par catégories - la consultation des articles - la gestion du
contenu via une interface d'administration

---

# Objectifs du projet

Les objectifs de ce projet sont :

-   créer une application web fonctionnelle avec **Django**
-   appliquer l'architecture **MVT (Model -- View -- Template)**
-   manipuler une base de données avec l'**ORM de Django**
-   créer une interface utilisateur **responsive avec Bootstrap**
-   comprendre la **structure d'un projet Django**

---

# Technologies utilisées

## Backend

-   Python
-   Django

## Frontend

-   HTML
-   CSS
-   Bootstrap

## Base de données

-   SQLite (base de données par défaut avec Django)

## Outils

-   Terminal / Invite de commandes
-   Navigateur Web
-   Éditeur de code (**VS Code recommandé**)

---

# Fonctionnalités du blog

## Gestion des articles

-   création d'articles
-   consultation des articles
-   affichage détaillé d'un article

## Gestion des catégories

-   associer un article à une catégorie
-   afficher la catégorie d'un article

## Interface utilisateur

-   page d'accueil listant les articles
-   page de détail d'un article
-   formulaire de publication d'article

## Interface administrateur

-   gestion des articles
-   gestion des catégories

---

# Architecture du projet

Le projet respecte l'architecture standard d'un projet Django.

    blog_project/
    │
    ├── blog_project
    │   ├── settings.py
    │   ├── urls.py
    │
    ├── blog
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── forms.py
    │   ├── admin.py
    │
    ├── templates
    │
    └── db.sqlite3

Le projet est composé de : - un **projet principal Django** - une
**application dédiée au blog**

---

# Installation du projet

## 1. Installer Python

Vérifier l'installation :

``` bash
python --version
```

## 2. Installer Django

``` bash
pip install django
```

## 3. Créer un projet Django

``` bash
django-admin startproject project_principal
cd project_principal
```

## 4. Lancer le serveur de développement

``` bash
python manage.py runserver
```

Puis ouvrir dans le navigateur :

    http://127.0.0.1:8000

---
# Création de l'application Blog

Créer l'application :

``` bash
python manage.py startapp blog
```

Ajouter l'application dans **settings.py** :

``` python
INSTALLED_APPS = [
    'blog',
]
```

---

# Conception de la base de données

## Modèle Catégorie

Une catégorie représente un thème d'article.

Exemples : 
- Technologie 
- Programmation 
- Jeux vidéo

Chaque catégorie contient : 
- un **nom**

## Modèle Article

Un article représente un contenu publié sur le blog.

Chaque article contient : 
- un **titre** 
- un **auteur** 
- un **contenu** 
- une **date de publication** 
- un **statut de publication** 
- une **catégorie**

### Relation

-   une **catégorie peut contenir plusieurs articles**
-   un **article appartient à une seule catégorie**

---

# Migration de la base de données

Après la création des modèles :

``` bash
python manage.py makemigrations
python manage.py migrate
```

---

# Interface d'administration

Django possède une interface d'administration intégrée.

Créer un compte administrateur :

``` bash
python manage.py createsuperuser
```

Accéder à l'administration :

    http://127.0.0.1:8000/admin/

---

# Création des vues

## Vue page d'accueil

Responsabilités : 
- récupérer tous les articles 
- trier les articles par date 
- envoyer les données au template

## Vue détail d'article

Responsabilités : 
- récupérer un article spécifique 
- afficher son contenu complet

## Vue création d'article

Responsabilités : 
- afficher un formulaire 
- valider les données 
- enregistrer l'article dans la base de données

---

# Gestion des URLs

Les URLs sont organisées en deux niveaux.

## URLs du projet

Inclure les URLs des applications.

## URLs de l'application

Définir les routes pour : 
- page d'accueil 
- détail d'article 
- création d'article

---

# Création des templates

Les templates représentent l'interface utilisateur.

### Page d'accueil

Affiche : 
- liste des articles 
- titre 
- auteur 
- catégorie 
- résumé 
- lien vers l'article complet

### Page détail

Affiche : 
- article complet 
- auteur 
- date de publication

### Page création d'article

Affiche : 
- formulaire 
- bouton de publication

---

# Intégration de Bootstrap

Bootstrap permet d'améliorer l'interface.

Éléments à styliser : 
- barre de navigation 
- cartes d'articles 
- boutons 
- formulaires

Objectif : obtenir une interface **moderne et responsive**.

---

# Tests du projet

Vérifier : 
- création d'articles 
- affichage des articles 
- affichage des détails 
- fonctionnement des catégories 
- fonctionnement du formulaire

Tester également l'interface administrateur.

---

# Améliorations possibles

-   système de commentaires
-   système d'utilisateurs
-   pagination des articles
-   recherche d'articles
-   filtres par catégories
-   système de tags
-   ajout d'images aux articles
-   système de likes

---
# Statut
- ✔ en cours de developpement
- ✔ creation du projet

---


# Résultat attendu

À la fin du projet, l'application doit permettre : 
- publier des articles 
- consulter les articles 
- classer les articles par catégorie 
- gérer le contenu via l'administration 
- afficher une interface responsive avec Bootstrap

---

# Auteur

**Codexx Nova**

GitHub :\
https://github.com/saphirbleu
