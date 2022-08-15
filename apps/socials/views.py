from django.shortcuts import render, get_object_or_404,redirect
from .models import Social
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core import settings
from PIL import Image



@login_required(login_url="user_login")
def generate_qr_code(request):
    template = "socials/socialmedialink.html"
    user = request.user
    if user.is_anonymous:
        messages.info(request, f"you are not authorized to view this page...")
        return redirect("qrcode_options")

    if request.method == "POST":
        qr_name = request.POST.get("qrcode-name")
        social_name = request.POST.get("name")
        social_link = request.POST.get("link")
        social_obj = Social.objects.create(name = qr_name, social_media_name = social_name, url = social_link,  created_by=user)
        if social_obj is not None:
            social_obj.save()

            qr_image_pdf = social_obj.name + "_" + str(social_obj.id) + ".pdf"

            image = Image.open(social_obj.qr_image)
            image.save(settings.MEDIA_ROOT + "/" + qr_image_pdf,format("PDF"))

            context = {
                "social_obj": social_obj,
                "social_obj_pdf": settings.MEDIA_URL + qr_image_pdf,
            }
            messages.success(request, f"qr code generated")
            return render(request, template, context)
        return redirect("social")
    return render(request, template)


def social_detail(request, social_id):
    template = "socials/socialmedialink.html"
    social_obj = get_object_or_404(Social, id=social_id)
    context = {"social_obj": social_obj}
    return render(request, template, context)