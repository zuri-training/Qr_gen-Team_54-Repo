from django.contrib import admin
from .models import Contacts


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "created_by", "name", "contact_name", "phone_no", "qr_image")
    readonly_fields = ("id", "qr_image")
