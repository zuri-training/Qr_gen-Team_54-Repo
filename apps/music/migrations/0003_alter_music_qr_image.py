# Generated by Django 4.0.6 on 2022-08-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="music",
            name="qr_image",
            field=models.ImageField(blank=True, null=True, upload_to="qrcodes"),
        ),
    ]
