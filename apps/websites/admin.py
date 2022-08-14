from django.contrib import admin
from .models import Website



@admin.register(Website)
class AdminWebsite(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'name', 'url', 'qr_image')
    readonly_fields = ('id', 'qr_image', 'qr_image_jpg', 'qr_image_pdf')