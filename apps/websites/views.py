from django.shortcuts import render

from .models import Website


def generate_qr_code(request):
    if request.method == "POST":
        Url = request.POST['url']
        Title = request.POST['title']
        Website.objects.create(url=Url, name=Title)

    qr_code = Website.objects.all()
    return render(request, "index.html", {'qr_code': qr_code})
