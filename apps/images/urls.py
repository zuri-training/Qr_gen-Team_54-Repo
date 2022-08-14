from django.urls import path
from .import views



urlpatterns = [
    path('generate-code/', views.generate_qr_code, name='image'),
    path('image-detail/<uuid:image_id>/', views.image_detail, name="image_detail")
]