from django.contrib import admin
from .models import Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'name', 'bank_name', 'account_name', 'account_number', 'qr_image')
    readonly_fields = ('id', 'qr_image')