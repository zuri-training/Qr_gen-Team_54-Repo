from .models import Video
from core import settings
from PIL import Image
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404




@login_required(login_url="user_login")
def generate_qr_code(request):
    template = "videos/video-upload.html"
    user = request.user
    if user.is_anonymous:
        messages.info(request, f"you are not authorized to view this page...")
        return redirect("home_page")

    if request.method == 'POST' and request.FILES['media-upload']:
        name = request.POST.get('qr-code-name')
        uploaded_file = request.FILES.get('media-upload')

        video_obj = Video.objects.create(name=name, file=uploaded_file, created_by=user)
        if video_obj is not None:
            video_obj.save()

            qr_image_pdf = video_obj.name + "_" + str(video_obj.id) + ".pdf"
            image = Image.open(video_obj.qr_image)
            image.save(settings.MEDIA_ROOT + "/" + qr_image_pdf,format("PDF"))

            context = {
                "video_obj": video_obj,
                "video_obj_pdf": settings.MEDIA_URL + qr_image_pdf,
            }
            messages.success(request, f"qr code successfully generated")
            return render(request, template, context)
        messages.error(request, f"input not supplied...")
        return redirect("video")
    return render(request, template)


def video_detail(request, video_id):
    template = "videos/mediadownload.html"
    video_obj = get_object_or_404(Video, id=video_id)
    context = {"video_obj":  video_obj}
    return render(request, template, context)