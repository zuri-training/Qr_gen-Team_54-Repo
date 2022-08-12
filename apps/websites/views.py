from django.shortcuts import render, redirect
from .models import Website
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required(login_url="user_login")
def generate_qr_code(request):
    user = request.user
    if user.is_anonymous:
        messages.info(request, f"you are not authorized to view this page...")
        return redirect("qrcode_options")
    template = "websites/Website-encode.html"
    if request.method == "POST":
        name = request.POST.get("name")
        url = request.POST.get("url")
        qr = Website.objects.create(name=name, url=url, created_by=user)
        if qr is not None:
            qr.save()
            messages.success(request, f"qr successfully generated")
            context = {"qr": qr}
            return render(request, template, context)
        messages.error(request, f"input not available")
        return redirect("website")
    return render(request, template)
