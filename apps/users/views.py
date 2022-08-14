from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser
from .validator import unauthenticated_user
from django.contrib.auth.decorators import login_required



# Create your views here.
@unauthenticated_user
def user_registration(request):
    template = 'users/signupindex.html'
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(f"FULLNAME = {fullname}")
        print(f"EMAIL = {email}")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "user with this email already exists")
            return redirect("user_login")
        user = CustomUser.objects.create(full_name=fullname, email=email)
        if user is not None:
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, "user successfully registered, proceed to login..")
            return redirect("user_login")
        messages.info(request, "empty form")
        return redirect("user_registration")
    return render(request, template)


@unauthenticated_user
def user_login(request):
    template = 'users/loginindex.html'
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"you are logged in as {user.full_name}")
            return redirect("qrcode_options")
        messages.info(request, f"login unsuccessful")
    return render(request, template)


@login_required(login_url="user_login")
def user_profile(request):
    user = request.user
    template = "users/profile.html"
    context = {"user":user}
    return render(request, template, context)


def user_logout(request):
    logout(request)
    messages.success(request, "user logged out successful")
    return redirect("home_page")