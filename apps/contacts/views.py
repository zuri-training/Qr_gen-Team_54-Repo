from django.shortcuts import render
from .models import Contacts
from django.contrib import messages


def generate_contact_qr_code(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact_name = request.POST.get("contact_name")
        phone_no = request.POST.get("phone_no")
        contact = Contacts.objects.create(
            name = name,
            contact_name = contact_name,
            phone_no = phone_no
        )
    if contact is not None:
        contact.save()
        context = {"contact": contact}
        messages.success(request, f"qr code generated")
        return render(request, "template_name", context)
        # return redirect("generate_code")
    return render(request, "template_name")