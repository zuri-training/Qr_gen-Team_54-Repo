from django.urls import path
from .import views



urlpatterns = [
    path('generate-code', views.generate_qr_code, name='music'),
    path('music-detail/<uuid:music_id>/', views.music_detail, name="music_detail")
]