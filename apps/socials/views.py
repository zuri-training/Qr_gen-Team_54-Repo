from django.shortcuts import render, get_object_or_404
from .models import Social



def generate_qr_code(request):
    template = "socials/socialmedialink.html"
    context = {}
    return render(request, template, context)


def social_detail(request, social_id):
    template = "socials/socialmedialink.html"
    social_obj = get_object_or_404(Social, id=social_id)
    context = {"social_obj": social_obj}
    return render(request, template, context)