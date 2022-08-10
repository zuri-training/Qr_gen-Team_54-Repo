import uuid
from django.db import models
from apps.users.models import CustomUser


class TimeStampModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    qr_image = models.ImageField(default='dummy qr.png', upload_to="qrcodes", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
