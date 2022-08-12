from django.urls import path
from .import views 



urlpatterns = [
    path('user-login/', views.user_login, name="user_login"),
    path('user-logout', views.user_logout, name="user_logout"),
    path('register/', views.user_registration, name="user_registration"),
]
