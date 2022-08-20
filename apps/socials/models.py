import qrcode
from io import BytesIO
from core import settings
from django.db import models
from django.urls import reverse
from django.core.files import File
from apps.common.models import TimeStampModel
from apps.common.choices import SOCIAL_CHOICES


class Social(TimeStampModel):
    name = models.CharField(max_length=255)
    social_media_name = models.CharField(choices=SOCIAL_CHOICES, max_length=150)
    url = models.URLField(default='https://')

    class Meta:
        ordering = ('-created_on',)
        verbose_name = 'Social media'
        verbose_name_plural = 'Social media'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("text_detail", kwargs={"id": self.id})

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(version=1, box_size=10, border=4, error_correction=qrcode.ERROR_CORRECT_L)
        qr_data = f'{settings.SITE_URL}{self.get_absolute_url()}'
        qr.add_data(qr_data)
        img = qr.make_image(fill="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, 'PNG')

        png_name = f'{self.created_by}_qr.png'
        jpg_name = f'{self.created_by}_qr.jpg'

        self.qr_image.save(png_name, File(buffer), save=False)
        self.qr_image_jpg.save(jpg_name, File(buffer), save=False)
        return super().save(*args, **kwargs)
    
    