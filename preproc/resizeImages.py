from PIL import Image
import os


sourceDir = "./colorferet/cropped_straight/"
targDir = './colorferet/resized/'

heights = []
weights = []
ratios = []

maxH = 180
maxW = 120

c = 0
for img in os.listdir(sourceDir):
    try:
        print(c)
        c += 1
        image = Image.open(sourceDir + img)
        height = image.size[1]
        weight = image.size[0]
        ratio = float(image.size[1])/float(image.size[0])

        if maxW * ratio <= maxH:
            newH = int(maxW * ratio)
            newW = maxW
        else:
            newW = int(ratio * maxH)
            newH = maxH

        resIm = image.resize((newW, newH), Image.LANCZOS)
        newim = Image.new('RGB', (120, 180))
        newim.paste(resIm)
        newim.save(targDir + img)
        
    except Exception as e:
        print(img, "died", e)
