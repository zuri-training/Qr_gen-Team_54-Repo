# Generated by Django 4.0.6 on 2022-08-03 21:19

import apps.common.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0004_alter_music_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="music",
            name="file",
            field=models.FileField(
                upload_to="media/songs/",
                validators=[apps.common.custom_validators.validate_mp3_file_type],
            ),
        ),
    ]
