import os
from PIL import Image



def convert_file_to_pdf_format(file):
    if file is not None:
        if file.split('.')[-1] in ['png', 'jpg']:
            file_name = os.path.basename(file).split('.')[-2]
            #file_name = file.split('.')
            image1 = Image.open(file)
            image_converted = image1.convert('RBG')
            image_converted.save('{0}.pdf'.format(file_name))
            return image_converted
       