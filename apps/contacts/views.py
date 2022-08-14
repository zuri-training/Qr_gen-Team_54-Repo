from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacts
from django.contrib import messages



def generate_qr_code(request):
    template = "contacts/contact-page.html"

    user = request.user
    if user.is_anonymous:
        messages.info(request, f"you are not authorized to view this page...")
        return redirect("qrcode_options")

    if request.method == "POST":
        name = request.POST.get("qr-code-name")
        contact_name = request.POST.get("contact-name")
        phone_no = request.POST.get("phone-number")

        contact_obj = Contacts.objects.create(
            name=name,
            contact_name=contact_name,
            phone_no=phone_no,
            created_by=user
        )
        if contact_obj is not None:
            contact_obj.save()
            context = {"contact_obj": contact_obj}
            messages.success(request, f"qr code generated")
            return render(request, template, context)
        return redirect("contact")
    return render(request, template)


def contact_detail(request, contact_id):
    template = "contacts/contact-page.html"
    contact_obj = get_object_or_404(Contacts, id=contact_id)
    context = {"contact_obj": contact_obj}
    return render(request, template, context)