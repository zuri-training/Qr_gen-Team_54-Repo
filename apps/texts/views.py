from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Text
from core import settings
from PIL import Image




@login_required(login_url="user_login")
def generate_qr_code(request):
    template = "texts/text-encode.html"
    user = request.user
    if user.is_anonymous:
        messages.info(request, f"you are not authorized to view this page...")
        return redirect("home_page")
    
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        text_obj = Text.objects.create(
            name=name,
            description=description,
            created_by=user
        )
        if text_obj is not None:
            text_obj.save()

            qr_image_pdf = text_obj.name + "_" + str(text_obj.id) + ".pdf"
            image = Image.open(text_obj.qr_image)
            image.save(settings.MEDIA_ROOT + "/" + qr_image_pdf,format("PDF"))

            context = {
                "text_obj": text_obj,
                "text_obj_pdf": settings.MEDIA_URL + qr_image_pdf,
            }
            return render(request, template, context)
        return redirect("text")
    return render(request, template)


def text_detail(request, text_id):
    template = "texts/textoutput.html"
    text_obj = get_object_or_404(Text, id=text_id)
    context = {"text_obj": text_obj}
    return render(request, template, context)