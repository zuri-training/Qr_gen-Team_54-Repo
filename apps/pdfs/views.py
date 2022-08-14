from django.shortcuts import render, redirect, get_object_or_404
from .models import Pdf
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="user_logoin")
def generate_qr_code(request):
    template = "pdfs/PDF-encode.html"
    user = request.user
    if user.is_anonymous:
        messages.info(request, f"you are not authorized to view this page...")
        return redirect("qrcode_options")

    if request.method == 'POST' and request.FILES['pdf_file']:
        name = request.POST.get('name')
        uploaded_file = request.FILES.get('pdf_file')

        pdf_obj = Pdf.objects.create(name=name, file=uploaded_file, created_by=user)
        if pdf_obj is not None:
            pdf_file = None
            pdf_obj.save()
            context = {
                "pdf_obj": pdf_obj,
                "qr_code_pdf": pdf_file,
            }
            messages.success(request, f"qr successfully generated")
            return render(request, template, context)
        messages.error(request, f"input not supplied...")
        return redirect("pdf")
    return render(request, template)


def pdf_detail(request, pdf_id):
    template = "pdfs/PDF-encode.html"
    pdf_obj = get_object_or_404(Pdf, id=pdf_id)
    context = {"pdf_obj": pdf_obj}
    return render(request, template, context)