from django.core.files import File
import qrcode
from io import BytesIO
from django.db import models
from django.urls import reverse
from apps.common.models import TimeStampModel
from apps.common.custom_validators import validate_mp3_file_type



class Music(TimeStampModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='songs/', validators=[validate_mp3_file_type])
    file_size = models.CharField(max_length=11)
    description = models.TextField()

    class Meta:
        ordering = ('-created_on',)
        verbose_name = 'Music'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('music_detail', kwargs={"music_id": self.id})

    def get_file_size(self, uploaded_file):
        if uploaded_file >= 1024 and uploaded_file < (1024**2):
            self.file_size = str(round(uploaded_file / 1000, 2)) + " KB"

        elif uploaded_file >= (1024**2) and uploaded_file < (1024**3):
            self.file_size = str(round(uploaded_file / (1000**2), 1)) + " MB"

        return self.file_size

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(version=1, box_size=10, border=4, error_correction=qrcode.ERROR_CORRECT_L)
        qr_data = f'{self.file}'
        qr.add_data(qr_data)
        img = qr.make_image(fill="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        file_name = f'{self.created_by}_{self.id}qr.png'
        self.qr_image.save(file_name, File(buffer), save=False)
        self.file_size = self.get_file_size(uploaded_file=self.file.size)
        return super().save(*args, **kwargs)