import os
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from PIL import Image
from core.settings import BASE_DIR



def convert_qr_code_image_to_pdf_format(path, created_by, filename):
    image_path = path.qr_image.path
    pdf_path = BASE_DIR / f"static/media/pdf/{image_path.split('.png')[0]}.pdf"
    image = Image.open(image_path)
    rgb_image = image.convert('RGB')
    pdf_image = rgb_image.save(pdf_path.replace('.png', '.pdf'), 'PDF')
    return image_path.replace('.png', '.pdf'), os.path.basename(pdf_path.replace('.png', '.pdf'))
    # pdf_path = BASE_DIR / f"static/media/pdf/{created_by}.pdf"
    # image_1 = Image.open(image.path)
    # im_1 = image_1.convert('RGB')
    # im_1.save(pdf_path)
    # print(f"PDF FILE PATH = {pdf_path}")
    # return pdf_path

def convert_to_pdf(qr_image):
    image_path = qr_image.path
    image = Image.open(image_path)
    rgb_image = image.convert('RGB')
    pdf_image = rgb_image.save(image_path.replace('.png', '.pdf'), 'PDF')
    return image_path.replace('.png', '.pdf'), os.path.basename(image_path.replace('.png', '.pdf'))
    # print(f"IMAGE PATH = {image.path}")
    # filename = image.name
    # qr_image_path = f'{image.path}'
    # with open(qr_image_path, 'wb') as f:
    #     f.write(image)

    # pdf_path = BASE_DIR / f'/static/media/pdf/{filename.split(".")[0]}.pdf'
    # image = Image.open(qr_image_path)
    # im = image.convert('RGB')
    # im.save(pdf_path)

    # fs = FileSystemStorage(pdf_path)
    # response = FileResponse(fs.open(pdf_path, 'rb'), content_type='application/pdf')
    # response['Content-Disposition'] = f'attachment; filename="{created_by}.pdf"'
    # return response
    # image = Image.open(path)
    # rgb_image = image.convert('RGB')
    # pdf_image = rgb_image.save(path.replace('.png', '.pdf'), 'PDF')
    # return path.replace('.png', '.pdf'), os.path.basename(path.replace('.png', '.pdf'))



# def export(self, request, *args, **kwargs):
#     uploaded_file = request.FILES['image']
#     filename = uploaded_file.name

#     temp_path = f'/tmp/{filename}'
#     with open(temp_path, 'wb') as f:
#         f.write(uploaded_file.read())

#     pdf_path = f'/tmp/{filename.split(".")[0]}.pdf'
#     image = Image.open(temp_path)
#     im = image.convert('RGB')
#     im.save(pdf_path)

#     fs = FileSystemStorage(pdf_path)
#     response = FileResponse(fs.open(pdf_path, 'rb'), content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="{uuid.uuid4().hex}.pdf"'
#     return response


# # modelled functions
# def convert_to_pdf(path):
#     image = Image.open(path)
#     rgb_image = image.convert('RGB')
#     pdf_image = rgb_image.save(path.replace('.png', '.pdf'), 'PDF')
#     return path.replace('.png', '.pdf'), os.path.basename(path.replace('.png', '.pdf'))


# def code_download_pdf(request, pk):
#     obj = get_object_or_404(Website.objects.filter(user=request.user), pk=pk)
#     filepath, filename = convert_to_pdf(obj.qr_code.path)
#     response = HttpResponse(open(filepath, 'rb').read(), content_type='application/force-download')
#     response['Content-Disposition'] = 'attachment; filename=%s' % filename
#     return response