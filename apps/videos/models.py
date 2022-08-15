import qrcode
from io import BytesIO
from django.db import models
from django.urls import reverse
from django.core.files import File
from apps.common.models import TimeStampModel
from apps.common.custom_validators import validate_video_file



class Video(TimeStampModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/', validators=[validate_video_file])
    file_size = models.CharField(max_length=11)
    description = models.TextField()

    class Meta:
        ordering = ('-created_on',)
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={"video_id": self.id})

    def get_file_size(self, uploaded_file):
        if uploaded_file >= 1024 and uploaded_file < (1024**2):
            self.file_size = str(round(uploaded_file / 1000, 2)) + " KB"

        elif uploaded_file >= (1024**2) and uploaded_file < (1024**3):
            self.file_size = str(round(uploaded_file / (1000**2), 1)) + " MB"

        return self.file_size

    def save(self, *args, **kwargs):
        self.file_size = self.get_file_size(uploaded_file=self.file.size)
        qr = qrcode.QRCode(version=1, box_size=10, border=4, error_correction=qrcode.ERROR_CORRECT_L)
        qr_data = f' http://qrx-gen.herokuapp.com{self.get_absolute_url()}'
        qr.add_data(qr_data)
        img = qr.make_image(fill="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, 'PNG')

        png_name = f'{self.created_by}_qr.png'
        jpg_name = f'{self.created_by}_qr.jpg'

    
        self.qr_image.save(png_name, File(buffer), save=False)
        self.qr_image_jpg.save(jpg_name, File(buffer), save=False)
       
        return super().save(*args, **kwargs)