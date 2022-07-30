from django.shortcuts import render


def test_project(request):
    template_name = "base.html"
    context = {}
    return render(request, template_name, context)