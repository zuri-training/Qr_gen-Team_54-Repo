from django.contrib import admin
from apps.users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from apps.users.forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class AdminCustomUser(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    ordering = ["email"]
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None,{
            "fields": ('email', 'password'),
        }),

        ('Details', {
            "fields": ('first_name', 'last_name', 'slug'),
        }),

        ('Permissions', {
            "fields": ('is_active', 'is_staff', 'is_superuser'),
        }),
    )