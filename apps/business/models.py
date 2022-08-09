import qrcode
from io import BytesIO
from django.db import models
from django.urls import reverse
from django.core.files import File
from apps.common.models import TimeStampModel
from apps.common.custom_validators import validate_phone_no_value_and_length



class Business(TimeStampModel):
    name = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    phone_no = models.CharField(max_length=11, validators=[validate_phone_no_value_and_length])
    location = models.CharField(max_length=255)
    bio = models.TextField()
    logo = models.ImageField()

    class Meta:
        ordering = ('-created_on',)
        verbose_name = 'Business'
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return self.business_name

    def get_absolute_url(self):
        return reverse('business_detail', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(version=1, box_size=10, border=4, error_correction=qrcode.ERROR_CORRECT_L)
        qr_data = f"{self.business_name}"
        qr.add_data(qr_data)
        img = qr.make_image(fill="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        file_name = f'{self.created_by}_{self.id}qr.png'
        self.qr_image.save(file_name, File(buffer), save=False)
        return super().save(*args, **kwargs)