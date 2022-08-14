from django.urls import path
from .import views



urlpatterns = [
    path('generate-code/', views.generate_qr_code, name='bank'),
    path('bank-detail/<uuid:bank_id>/', views.bank_detail, name="bank_detail")
]