from django.urls import path
from .import views



urlpatterns = [
    path('generate-code/', views.generate_qr_code, name='business'),
    path('business-detail/<uuid:business_id>/', views.business_detail, name="business_detail")
]