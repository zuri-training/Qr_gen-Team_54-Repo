from django.urls import path
from .import views



urlpatterns = [
    path('generate-code/', views.generate_qr_code, name='contact'),
    path('contact-detail/<uuid:contact_id>/', views.contact_detail, name='contact_detail')
]