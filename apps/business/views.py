from .models import Business
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


@login_required(login_url="user_login")
def generate_qr_code(request):
    template = "business/business.html"
    
    user = request.user
    if user.is_anonymous:
        messages.info(request, f"you are not authorized to view this page...")
        return redirect("home_page")

    if request.method == "POST" and request.FILES["logo"]:
        business_name = request.POST.get("business-name")
        email = request.POST.get("email_address")
        phone_no = request.POST.get("phone_no")
        location = request.POST.get("location")
        description = request.POST.get("description")
        logo = request.FILES.get("logo")

        business_obj = Business.objects.create(
            business_name=business_name,
            email=email,
            phone_no=phone_no,
            location=location,
            bio=description,
            logo=logo,
            created_by=user
        )
        if business_obj is not None:
            business_obj.save()
            context = {"business_obj": business_obj}
            
            messages.success(request, f"qr code generated successfully")
            return render(request, template, context)
        messages.info(request, f"error generating qr code please try again...")
        return redirect("business")
    return render(request, template)


def business_detail(request, business_id):
    template = "business/businessoutput.html"
    business_obj = get_object_or_404(Business, id=business_id)
    context = {"business_obj": business_obj}
    return render(request, template, context)