# import PIL as PIL
from PIL import Image
from PIL import ImageOps
# import sys
import os

images_in_directory = []
path = os.getcwd()
# os.mkdir(path+"Out")
# path = path + "/"
with os.scandir(path) as it:
    for entry in it:
        if entry.name.endswith(".jpg") and entry.is_file():
            print(entry.name)#, entry.path)
            images_in_directory.append(entry.name)


for image in images_in_directory:
    in_file = image
    out_file = 'out-' + image

    img = Image.open(in_file)
    width, height = img.size

    # crop (left, top, right, bottom)

    difference = int(abs((width-height) / 2))
    if(width >= height):
        border = (0, difference, 0, difference)
    else:
        border = (difference, 0, difference, 0)

    # cropped = img.crop((10, -5000, width-30, height-40))
    cropped = ImageOps.expand(img, border=border, fill="white")
    cropped.save(out_file)
