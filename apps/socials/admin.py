from django.contrib import admin
from .models import Social


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("id", "created_by", "social_media_name", "url", "qr_image")
    readonly_fields = ("id", "qr_image")
