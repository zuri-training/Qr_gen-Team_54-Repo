from django.shortcuts import render, get_object_or_404
from .models import Image
from django.contrib.auth.decorators import login_required




@login_required(login_url="user_login")
def generate_qr_code(request):
    template = "images/picture-upload.html"
    context = {}
    return render(request, template, context)


def image_detail(request, image_id):
    template = "images/picture-upload.html"
    image_obj = get_object_or_404(Image, id=image_id)
    context = {"image_obj": image_obj}
    return render(request, template, context)