from .models import Bank
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def bank_detail(request, bank_id):
    template = "banks/bankaccount.html"
    bank_obj = get_object_or_404(Bank, id=bank_id)
    context = {"bank_obj": bank_obj}
    return render(request, template, context)


@login_required(login_url="user_login")
def generate_qr_code(request):
    template = "banks/bankaccount.html"
    user = request.user
    if user.is_anonymous:
        messages.info(request, f"you are not authorized to view this page...")
        return redirect("qrcode_options")

    if request.method == "POST":
        name = request.POST.get("name")
        account_name = request.POST.get("account_name")
        bank_name = request.POST.get("bank_name")
        account_no = request.POST.get("account_no")

        url = request.POST.get("url")
        bank_obj = Bank.objects.create(
            name=name,
            account_name=account_name,
            bank_name=bank_name,
            account_number=account_no,
            created_by=user
        )
        if bank_obj is not None:
            pdf_file = None
            bank_obj.save()
            context = {
                "bank_obj": bank_obj,
                "qr_code_pdf": pdf_file,
            }
            messages.success(request, f"qr successfully generated")
            return render(request, template, context)
        messages.error(request, f"input not available")
        return redirect("bank")
    return render(request, template)
