from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def register(request):
    return HttpResponse('hello there')


def user_login(request):
    pass


def user_logout(request):
    pass