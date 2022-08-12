import qrcode
from io import BytesIO
from django.db import models
from django.urls import reverse
from django.core.files import File
from apps.common.models import TimeStampModel
from apps.common.custom_validators import validate_value_type_and_length



class Bank(TimeStampModel):
    name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=150)
    bank_name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=10, validators=[validate_value_type_and_length])

    class Meta:
        ordering = ('created_on',)
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bank_detail', kwargs={"bank_id": self.id})

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(version=1, box_size=10, border=4, error_correction=qrcode.ERROR_CORRECT_L)
        qr_data = f"{self.url}"
        qr.add_data(qr_data)
        img = qr.make_image(fill="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        file_name = f'{self.created_by}_{self.id}qr.png'
        self.qr_image.save(file_name, File(buffer), save=False)
        return super().save(*args, **kwargs)
