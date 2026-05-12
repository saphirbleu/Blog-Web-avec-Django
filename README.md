# 📘 Projet Blog Django

## 📋 Description du projet

Application web de **blog** permettant de publier et consulter des articles.

Voir le détail complet dans le [cahier de charges](CAHIER_DE_CHARGE.md)

---

## 🎯 Objectifs

- Créer une application web fonctionnelle avec **Django**
- Appliquer l'architecture **MVT (Model - View - Template)**
- Manipuler une base de données avec l'**ORM de Django**
- Créer une interface utilisateur **responsive avec Bootstrap**
- Gérer l'authentification des utilisateurs

Pour plus de détails, consultez le [cahier de charges](CAHIER_DE_CHARGE.md)

---

## 🏗️ Architecture du projet

### Structure des dossiers

```
Projet Django/
├── blog/                          # Application blog
│   ├── migrations/                # Migrations de la BD
│   ├── static/blog/               # Fichiers statiques (CSS, JS, images)
│   ├── templates/blog/            # Templates HTML
│   │   ├── accueil.html           # Page d'accueil du blog
│   │   ├── ajouter_article.html   # Formulaire d'ajout d'article
│   │   ├── details.html           # Page de détails d'un article
│   │   └── base.html              # Template de base
│   ├── admin.py                   # Configuration admin
│   ├── apps.py                    # Configuration de l'app
│   ├── models.py                  # Modèles de données
│   ├── tests.py                   # Tests unitaires
│   ├── urls.py                    # URLs de l'app
│   └── views.py                   # Vues/contrôleurs
│
├── users/                         # Application utilisateurs
│   ├── migrations/                # Migrations de la BD
│   ├── static/users/              # Fichiers statiques
│   │   └── style.css              # Styles des pages utilisateurs
│   ├── templates/users/           # Templates HTML
│   │   ├── login.html             # Page de connexion
│   │   └── register.html          # Page d'inscription
│   ├── admin.py                   # Configuration admin
│   ├── apps.py                    # Configuration de l'app
│   ├── models.py                  # Modèles de données
│   ├── tests.py                   # Tests unitaires
│   ├── urls.py                    # URLs de l'app
│   └── views.py                   # Vues/contrôleurs
│
├── projet_principal/              # Configuration principale du projet
│   ├── urls.py                    # Routage principal des URLs
│   ├── settings.py                # Paramètres du projet (BD, apps, etc.)
│   ├── asgi.py                    # Configuration ASGI
│   └── wsgi.py                    # Configuration WSGI
│
├── manage.py                      # Utilitaire de gestion Django
├── db.sqlite3                     # Base de données SQLite
├── README.md                      # Ce fichier
├── CAHIER_DE_CHARGE.md            # Cahier des charges détaillé
└── LICENSE                        # Licence du projet
```

### Applications Django

| Application | Description |
|-------------|-------------|
| **blog** | Gestion des articles, affichage des articles, interfaces de consultation |
| **users** | Gestion des utilisateurs, authentification, inscription |

---

## 💻 Technologies utilisées

### Backend
- **Python** - Langage de programmation
- **Django** - Framework web MVC
- **SQLite** - Base de données

### Frontend
- **HTML5** - Structure des pages
- **CSS3** - Styles
- **Bootstrap** - Framework CSS responsive

### Outils
- **Terminal / PowerShell** - Ligne de commande
- **VS Code** - Éditeur de code
- **Git** - Contrôle de version

---

## ✅ Avancement du projet

| Étape | Statut |
|-------|--------|
| Initialisation du projet Django | ✔️ |
| Création des applications (blog, users) | ✔️ |
| Configuration des applications dans `settings.py` | ✔️ |
| Configuration de l'interface admin | ✔️ |
| Modèles de données | ✔️ |
| Migrations de base de données | ✔️ |
| Vues et contrôleurs | ✔️ |
| Routage des URLs | ✔️ |
| Templates HTML/CSS | ✔️ |
| Authentification utilisateurs | ✔️ |
| Interface responsive | ✔️ |

---

## 🌐 URLs importantes

Une fois le serveur lancé, accédez aux URLs suivantes :

| URL | Description |
|-----|-------------|
| [http://127.0.0.1:8000/](http://127.0.0.1:8000/) | Page d'accueil |
| [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/) | Liste des articles du blog |
| [http://127.0.0.1:8000/blog/ajouter/](http://127.0.0.1:8000/blog/ajouter/) | Ajouter un nouvel article |
| [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) | Interface d'administration |
| [http://127.0.0.1:8000/users/login/](http://127.0.0.1:8000/users/login/) | Connexion utilisateur |
| [http://127.0.0.1:8000/users/register/](http://127.0.0.1:8000/users/register/) | Inscription utilisateur |

---

## 🚀 Installation et utilisation

### 1️⃣ Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### 2️⃣ Cloner le projet

```bash
git clone https://github.com/saphirbleu/Blog-Web-avec-Django.git
cd Blog-Web-avec-Django
```

### 3️⃣ Créer et activer un environnement virtuel

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 4️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5️⃣ Appliquer les migrations

```bash
python manage.py migrate
```

### 6️⃣ Lancer le serveur Django

```bash
python manage.py runserver
```
---

## 📝 Fonctionnalités

### Blog
- ✅ Affichage des articles
- ✅ Détails des articles
- ✅ Ajouter/Modifier/Supprimer des articles (interface admin)
- ✅ Pagination des articles

### Users
- ✅ Inscription des utilisateurs
- ✅ Connexion sécurisée
- ✅ Gestion des profils (interface admin)

---

## 📚 Ressources utiles

- [Documentation Django](https://docs.djangoproject.com/)
- [Documentation Bootstrap](https://getbootstrap.com/docs/)
- [Tutoriels Django en français](https://www.django-rest-framework.org/)

---

## 📄 Licence

Ce projet est sous licence [MIT](LICENSE)