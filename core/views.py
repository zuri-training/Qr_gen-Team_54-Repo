from django.shortcuts import render
from django.contrib.auth.decorators import login_required




def site_home(request):
    template_name = "index.html"
    return render(request, template_name)


# @login_required(login_url="user_login")
def qr_code_options(request):
    template = 'qrcode_options.html'
    return render(request, template)


def about_us(request):
    template = "aboutUs.html"
    return render(request, template)


def site_terms(request):
    template = "terms.html"
    return render(request, template)


def site_feedback(request):
    template = "feedback.html"
    return render(request, template)


def faq(request):
    template = "faq-page.html"
    return render(request, template)


def site_draft(request):
    template = "draft.html"
    return render(request, template)


def user_profile(request):
    template = "profile.html"
    return render(request, template)