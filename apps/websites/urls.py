from django.urls import path
from .import views



urlpatterns = [
    path('generate-code/', views.generate_qr_code, name='website'),
    path('website-detail/<uuid:website_id>/', views.website_detail, name='website_detail')
]