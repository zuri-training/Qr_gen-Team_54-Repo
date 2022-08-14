from .models import Website
from core import settings
from PIL import Image
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def website_detail(request, website_id):
    template = "websites/website_detail"
    website = get_object_or_404(Website, id=website_id)
    context = {"website": website}
    return render(request, template, context)


@login_required(login_url="user_login")
def generate_qr_code(request):
    template = "websites/Website-encode.html"
    user = request.user
    if user.is_anonymous:
        messages.info(request, f"you are not authorized to view this page...")
        return redirect("qrcode_options")

    if request.method == "POST":
        name = request.POST.get("name")
        url = request.POST.get("url")
        website_obj = Website.objects.create(name=name, url=url, created_by=user)
        if website_obj is not None:
            website_obj.save()

            qr_image_pdf = website_obj.name + "_" + str(website_obj.id) + ".pdf"
            image = Image.open(website_obj.qr_image)
            image.save(settings.MEDIA_ROOT + "/" + qr_image_pdf,format("PDF"))

            context = {
                "website_obj": website_obj,
                "website_obj_pdf": settings.MEDIA_URL + qr_image_pdf,
            }
            messages.success(request, f"qr successfully generated")
            return render(request, template, context)
        messages.error(request, f"input not available")
        return redirect("website")
    return render(request, template)
