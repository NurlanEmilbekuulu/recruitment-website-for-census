from io import BytesIO

import piexif as piexif
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


# def crop()

def rotate_image(image):
    file = None
    buffer = BytesIO()
    if "exif" in image.info:
        exif_dict = piexif.load(image.info["exif"])

        if piexif.ImageIFD.Orientation in exif_dict["0th"]:
            orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
            exif_bytes = piexif.dump(exif_dict)
            print(orientation)
            if orientation == 2:
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 3:
                image = image.rotate(180)
            elif orientation == 4:
                image = image.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 5:
                image = image.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 6:
                image = image.rotate(-90, expand=True)
            elif orientation == 7:
                image = image.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 8:
                image = image.rotate(90, expand=True)

            image.crop((1, 1, 10, 10))
            image.save(buffer, exif=exif_bytes)
            filename = 'profile.jpg'
            file = InMemoryUploadedFile(
                buffer, None, filename, 'image/png', buffer.tell(), None
            )
    return file
