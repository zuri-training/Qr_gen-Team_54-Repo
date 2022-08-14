from django.urls import path
from .import views



urlpatterns = [
    path('social/', views.generate_qr_code, name='social'),
    path('social-detail/<uuid:social_id>/', views.social_detail, name="social_detail")
]