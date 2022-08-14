from django.urls import path
from .import views



urlpatterns = [
    path('generate-code/', views.generate_qr_code, name='pdf'),
    path('pdf-detail/<uuid:pdf_id>/', views.pdf_detail, name="pdf_detail")
]