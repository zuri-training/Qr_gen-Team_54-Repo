from django.urls import path
from .import views



urlpatterns = [
    path('generate-code/', views.generate_qr_code, name='text'),
    path('text-detail/<uuid:text_id>/', views.text_detail, name='text_detail')
]