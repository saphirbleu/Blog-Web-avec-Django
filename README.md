# 📘 Projet Blog Django

## Description du projet

Voir le [cahier de charges](CAHIER_DE_CHARGE.md)

---

## Objectif

Voir le [cahier de charges](CAHIER_DE_CHARGE.md)

---

## Avancement

| Étape | Statut |
|-------|--------|
| Créer le projet | ✔ |
| Créer une application | ✔ |
| Ajouter l'app dans `settings.py` | ✔ |
| Configurer l'interface admin | ✔ |
| Ajouter des données dans l'interface admin | ✔ |
| Gérer le modèle | ✔ |
| Gérer les migrations | ✔ |
| Gérer les vues | ✔  |
| Gérer les URLs | ✔  |
| Gérer les templates | ✔  |
| Afficher les données sur une page HTML | ✔  |

---

## URLs importantes

- Admin : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

- blog : [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)  

---

## Installation et utilisation

### 1️⃣ Cloner le projet

```bash
https://github.com/saphirbleu/Blog-Web-avec-Django.git
cd Blog-Web-avec-Django

2️⃣ Créer et activer un environnement virtuel
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate

3️⃣ Installer les dépendances
```bash
pip install -r requirements.txt

4️⃣ Appliquer les migrations
```bash
python manage.py migrate

5️⃣ Créer un compte test unique
```bash
python create_test_user.py

✅ Exemple de sortie :

Compte créé : testuser482 | Mot de passe : test1234
Vous pouvez vous connecter à l'admin avec ce compte.
6️⃣ Lancer le serveur Django
```bash
python manage.py runserver

7️⃣ Se connecter à l’admin
URL : http://127.0.0.1:8000/admin/
Username : testuser482
Password : test1234