from django.urls import path
from .import views



urlpatterns = [
    path('generate-code', views.generate_qr_code, name='website')
]