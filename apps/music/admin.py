from django.contrib import admin
from .models import Music


@admin.register(Music)
class AdminMusic(admin.ModelAdmin):
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
