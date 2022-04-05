from PIL import Image
import os.path, sys

path = "rplace_arch_images_here"
cropped = "rplace_arch_images_here\\cropped"
resized = "rplace_arch_images_here\\cropped\\resized"
dirs = os.listdir(path)

counter = 0

def cropAndResize(counter: int):
    for item in dirs:
        fullpath = os.path.join(path,item)         #corrected
        if os.path.isfile(fullpath):

            counter += 1

            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((535, 70, 894, 252)) #corrected
            imCrop.save(cropped + "\\cropped_" + item, "PNG", quality=100)
            
            basewidth = 3840
            wpercent = (basewidth/float(imCrop.size[0]))
            hsize = int((float(imCrop.size[1])*float(wpercent)))
            img = imCrop.resize((basewidth,hsize), Image.NEAREST)
            img.save(resized + "\\resized_" + item, "PNG", quality=100)
            print(str(counter) + " done out of 10411")

cropAndResize(0)