from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Text




@login_required()
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
            context = {"text_obj": text_obj}
            return render(request, template, context)
        return redirect("business")
    return render(request, template)


def text_detail(request, text_id):
    template = "texts/text-encode.html"
    text_obj = get_object_or_404(Text, id=text_id)
    context = {"text_obj": text_obj}
    return render(request, template, context)