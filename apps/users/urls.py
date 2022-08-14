from django.urls import path
from .import views 



urlpatterns = [
    path('register/', views.user_registration, name="user_registration"),
    path('user-login/', views.user_login, name="user_login"),
    path('profile/', views.user_profile, name="profile"),
    path('user-logout/', views.user_logout, name="user_logout"),
]
