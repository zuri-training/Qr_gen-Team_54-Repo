from .models import CustomUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


# User registration view
def register(request):
    template_name = "users/register.html"
    if request.method == "POST":
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        confirm_password = request.POST.get("confirm_password", None)

        if CustomUser.objects.filter(email=email).exists():
            messages.INFO(request, f"Account already exist...")
            return redirect("register")

        if password != confirm_password:
            messages.warning(request, "passwords do not match...")
            return redirect("register")

        user = CustomUser.objects.create_user(
            first_name=first_name, last_name=last_name, email=email
        )
        user.set_password(password)
        user.save()
        messages.success(request, f"registration successful..")
        return redirect("homme")
    return render(request, template_name)


# user login view
def user_login(request):
    template_name = "users/login.html"
    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        user = authenticate(email=email, password=password)
        login(request, user)
        messages.success(request, f"User successfully logged in")
        return redirect("dashboard")
    return render(request, template_name)


# user logout view
def user_logout(request):
    if request.method == "GET":
        logout(request)
        return redirect("home")
