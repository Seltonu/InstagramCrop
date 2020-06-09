# import PIL as PIL
from PIL import Image
from PIL import ImageOps
import sys
import os

images_to_modify = []
path = os.getcwd()
filetypes = (".jpg", ".png", ".jpeg", ".gif", ".tiff", ".bmp", ".webp")
values_given = False
border_color = "white"
# os.mkdir(path+"Out")
# path = path + "/"

if(len(sys.argv) > 1):
    for arg in sys.argv:
        # print(arg)
        if(arg == "-w" or arg == "-white"):
            pass
        elif(arg == "-b" or arg == "-black"):
            border_color = "black"
            print("Border will be set black")
        elif(arg == "-blue"):
            border_color = "blue"
            print("Border will be set blue")
        elif(arg == "-r" or arg == "-red"):
            border_color = "red"
            print("Border will be set red")
        elif(arg == "-y" or arg == "-yellow"):
            border_color = "yellow"
            print("Border will be set yellow")
        elif(arg == "-green"):
            border_color = "green"
            print("Border will be set green")
        elif(arg == "-g" or arg == "-grey" or "-gray"):
            border_color = "gray"
            print("Border will be set grey")
        else:
            # values_given = True
            images_to_modify.append(arg)

    #remove first element which is program name, then check if images were passed
    # images_to_modify.pop(0)
    if(len(images_to_modify)):
        values_given = True

if(values_given):
    print("values given")
    for image in images_to_modify:
        if(not os.path.isfile(image)):
            images_to_modify.remove(image)
            print(image + " is not a valid file.")
else:
    print("values not given")
    with os.scandir(path) as it:
        for entry in it:
            if entry.name.endswith(filetypes) and entry.is_file():
                # print(entry.name)#, entry.path)
                images_to_modify.append(entry.name)

#create subdirectory to store results
if(not os.path.isdir("SQUARES")):
    os.mkdir("SQUARES")


# print("looping list " + str(images_to_modify))
for image in images_to_modify:
    in_file = image
    out_file = 'out-' + image

    img = Image.open(in_file)
    print("Proccessing " + in_file, end = "")
    width, height = img.size
    print(".", end="")

    difference = int(abs((width-height) / 2))
    if(width >= height):
        border = (0, difference, 0, difference)
    else:
        border = (difference, 0, difference, 0)
    print(".", end="")

    # crop is formatted (left, top, right, bottom), but passed as a tuple
    cropped = ImageOps.expand(img, border=border, fill=border_color)
    print(".", end="")

    #move to directory to save, and back out
    os.chdir("SQUARES")
    cropped.save(out_file)
    os.chdir(path)
    print(" done!")
