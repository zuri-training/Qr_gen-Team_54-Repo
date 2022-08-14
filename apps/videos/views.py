from .models import Video
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
            pdf_file = None
            video_obj.save()
            context = {
                "video_obj": video_obj,
                "qr_code_pdf": pdf_file,
            }
            messages.success(request, f"qr code successfully generated")
            return render(request, template, context)
        messages.error(request, f"input not supplied...")
        return redirect("video")
    return render(request, template)


def video_detail(request, video_id):
    template = "videos/video-upload.html"
    video_obj = get_object_or_404(Video, id=video_id)
    context = {" video_obj":  video_obj}
    return render(request, template, context)