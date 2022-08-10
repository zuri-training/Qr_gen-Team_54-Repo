from django.urls import path
from .views import generate_text_qr_code, get_text_qr_code


urlpatterns = [
    path("generate-code/", generate_text_qr_code, name="generate_code"),
    path("qr-info/<uuid:id>/", get_text_qr_code, name="text_detail"),
]
