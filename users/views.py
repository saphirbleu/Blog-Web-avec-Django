from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("accueil")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")

    return render(request, "users/login.html")


# REGISTER
def register_view(request):
    if request.method == "POST":
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # Vérification champs
        if not all([last_name, first_name, email, username, password, password2]):
            messages.error(request, "Tous les champs sont obligatoires")
            return redirect("register")

        if password != password2:
            messages.error(request, "Les mots de passe ne correspondent pas")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email déjà utilisé")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nom d'utilisateur déjà pris")
            return redirect("register")

        # Création utilisateur
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        login(request, user)
        return redirect("accueil")

    return render(request, "users/register.html")

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect("login")