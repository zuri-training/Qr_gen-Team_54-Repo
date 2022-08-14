from django.urls import path
from .import views



urlpatterns = [
    path('generate-code/', views.generate_qr_code, name='video'),
    path('video-detail/<uuid:video_id>/', views.video_detail, name="video_detail")
]