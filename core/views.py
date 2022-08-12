from django.shortcuts import render
from django.contrib.auth.decorators import login_required




def site_home(request):
    template_name = "index.html"
    return render(request, template_name)


@login_required(login_url="user_login")
def qr_code_options(request):
    template = 'qrcode_options.html'
    return render(request, template)
