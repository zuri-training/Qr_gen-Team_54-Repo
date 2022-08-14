# Generated by Django 4.0.6 on 2022-08-13 08:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qr_image', models.ImageField(blank=True, null=True, upload_to='qrcodes')),
                ('qr_image_pdf', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('qr_image_jpg', models.ImageField(blank=True, null=True, upload_to='jpg')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texts',
                'ordering': ('-created_on',),
            },
        ),
    ]
