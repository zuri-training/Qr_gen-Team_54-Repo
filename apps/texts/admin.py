from django.contrib import admin
from .models import Text


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'name', 'description', 'qr_image')
    readonly_fields = ('id', 'qr_image', 'qr_image_jpg', 'qr_image_pdf')