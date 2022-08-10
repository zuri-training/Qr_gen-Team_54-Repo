import mimetypes
from core import settings
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage


# this checks value type and length of value supplied
def validate_value_type_and_length(input):
    if type(input) != int:
        raise ValidationError("input must be a whole number..")
    if len(input) < 10:
        raise ValidationError("input cannot be less than 10 in length...")


# this checks for phone number type and length
def validate_phone_no_value_and_length(input):

    if len(input) < 11:
        raise ValidationError("input cannot be less than 11 in length...")

        # if type(input) != int:
        raise ValidationError("input must be a whole number..")


# this ensures users don't proceed without uploading a pdf file and not more than 10mb in size,
def validate_pdf_file_type(input):
    pdf_file_types = ["application/pdf"]

    if not input:
        raise ValidationError("No file selected, please select a file...")

    if input.size > settings.MAX_VIDEO_FILE_SIZE:
        raise ValidationError("Upload Error, File cannot be larger than 100MB.")

    fs = FileSystemStorage()
    filename = fs.save(input.name, input)
    file_type = mimetypes.guess_type(filename)[0]

    if file_type not in pdf_file_types:
        raise ValidationError(
            "Upload Error, File must be a pdf file, please try again."
        )


# this ensures users don't proceed without uploading an mp3 file and not more than 10mb in size,
def validate_mp3_file_type(input):
    audio_file_types = ["audio/mp3", "audio/mpeg"]

    if not input:
        raise ValidationError("No file selected")

    if input.size > settings.MAX_MUSIC_PDF_FILE_SIZE:
        raise ValidationError("file cannot be larger than 10MB.")

    fs = FileSystemStorage()
    filename = fs.save(input.name, input)
    file_type = mimetypes.guess_type(filename)[0]

    if file_type not in audio_file_types:
        raise ValidationError(
            "Upload Error, file must be an mp3 file, please try again."
        )


# this ensures users don't proceed without upload an image file and not more than 10mb in size.
def validate_image_file_type(input):
    image_file_types = ["image/png", "image/jpg", "image/jpeg"]

    if not input:
        raise ValidationError("No file selected")

    if input.size > settings.MAX_MUSIC_PDF_FILE_SIZE:
        raise ValidationError("file cannot be larger than 10MB.")

    fs = FileSystemStorage()
    filename = fs.save(input.name, input)
    file_type = mimetypes.guess_type(filename)[0]

    if file_type not in image_file_types:
        raise ValidationError(
            "Upload Error, file must be an image file, please try again."
        )


# this ensures users don't proceed without uploading a video file and not more than 100mb in size.
def validate_video_file(input):
    video_file_types = [
        "video/mp4",
        "video/webdl",
        "video/avi",
        "video/wmv",
        "video/mkv",
    ]

    if not input:
        raise ValidationError("No file selected, please select a file...")

    if input.size > settings.MAX_VIDEO_FILE_SIZE:
        raise ValidationError(
            f"Upload Error, file size is {round(input.size/(1024**2),1)}MB and cannot be larger than 100MB."
        )

    fs = FileSystemStorage()
    filename = fs.save(input.name, input)
    file_type = mimetypes.guess_type(filename)[0]

    if file_type not in video_file_types:
        raise ValidationError(
            "Upload Error, File must be an video file, please try again."
        )
