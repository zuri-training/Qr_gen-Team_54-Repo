# Generated by Django 4.0.6 on 2022-08-03 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("websites", "0002_alter_website_qr_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="website",
            old_name="qr_code",
            new_name="file",
        ),
    ]
