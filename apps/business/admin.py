from django.contrib import admin
from .models import Business


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_by",
        "name",
        "business_name",
        "email",
        "phone_no",
        "qr_image",
    )
    readonly_fields = ("id", "qr_image")
