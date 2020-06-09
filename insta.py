# import PIL as PIL
from PIL import Image
from PIL import ImageOps
import sys
import os

images_to_modify = []
path = os.getcwd()
filetypes = (".jpg", ".png", ".jpeg", ".gif", ".tiff", ".bmp", ".webp")
# os.mkdir(path+"Out")
# path = path + "/"

if(len(sys.argv) > 1):
    values_given = True
    for arg in sys.argv:
        # print(arg)
        images_to_modify.append(arg)
    images_to_modify.pop(0) #remove first element which is program name

if(values_given):
    for image in images_to_modify:
        if(not os.path.isfile(image)):
            images_to_modify.remove(image)
            print(image + " is not a valid file.")
else:
    with os.scandir(path) as it:
        for entry in it:
            if entry.name.endswith(filetypes) and entry.is_file():
                # print(entry.name)#, entry.path)
                images_to_modify.append(entry.name)



# print("looping list " + str(images_to_modify))
for image in images_to_modify:
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
