from django.contrib import admin
from .models import Pdf


@admin.register(Pdf)
class AdminPdf(admin.ModelAdmin):
    list_display = (
        "id",
        "created_by",
        "name",
        "file",
        "file_size",
        "description",
        "qr_image",
    )
    readonly_fields = ("id", "qr_image", "file_size")
