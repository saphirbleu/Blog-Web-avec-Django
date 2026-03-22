import os
import django
import random
import string

# 1️⃣ Initialiser Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monprojet.settings')  # <-- remplace par le nom de ton projet
django.setup()

from django.contrib.auth.models import User

# 2️⃣ Fonction pour générer un username unique
def random_username(prefix="testuser"):
    suffix = ''.join(random.choices(string.digits, k=3))
    return f"{prefix}{suffix}"

# 3️⃣ Créer le compte test
username = random_username()
password = "test1234"  # mot de passe fictif

# Vérifie si le compte existe déjà
while User.objects.filter(username=username).exists():
    username = random_username()

user = User.objects.create_user(username=username, password=password, is_staff=True)
print(f"Compte créé : {username} | Mot de passe : {password}")
print("Vous pouvez vous connecter à l'admin avec ce compte.")