from PIL import Image
import os

baseDir = "/home/tejvi/Documents/colorferet/dec/"
targDir = "/home/tejvi/Documents/colorferet/dec_jpg/"

c = 0

for img in os.listdir(baseDir):
    try:
        image = Image.open(baseDir + img)
        image.save(targDir + img[:-3] + 'jpg')
        print(c)
        c += 1
    except:
        print(img, "DIED")
