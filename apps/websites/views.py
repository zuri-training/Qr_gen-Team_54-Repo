from django.shortcuts import render, redirect, get_object_or_404
from .models import Website
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.common.converter import convert_file_to_pdf_format


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
        qr = Website.objects.create(name=name, url=url, created_by=user)
        if qr is not None:
            qr.save()
            messages.success(request, f"qr successfully generated")
            qr_code_pdf = convert_file_to_pdf_format(file=qr.qr_image)
            context = {
                "qr": qr,
                "qr_code_pdf": qr_code_pdf
            }
            return render(request, template, context)
        messages.error(request, f"input not available")
        return redirect("website")
    return render(request, template)
