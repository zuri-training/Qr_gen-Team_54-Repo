from .models import Music
from apps.common import converter
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404



def music_detail(request, music_id):
    template = "music/music-upload.html"
    music_obj = get_object_or_404(Music, id=music_id)
    context = {"music_obj": music_obj}
    return render(request, template, context)


@login_required(login_url="user_login")
def generate_qr_code(request):
    template = "music/music-upload.html"
    user = request.user
    if user.is_anonymous:
        messages.info(request, f"you are not authorized to view this page...")
        return redirect("qrcode_options")

    if request.method == "POST":
        name = request.POST.get("name")
        url = request.POST.get("url")
        music_obj = Music.objects.create(name=name, url=url, created_by=user)
        if music_obj is not None:
            music_obj.save()
            context = {"music_obj": music_obj}
            messages.success(request, f"qr successfully generated")
            return render(request, template, context)
        messages.error(request, f"input not available")
        return redirect("website")
    return render(request, template)
