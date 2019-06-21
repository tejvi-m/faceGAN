import os
from cv2 import imread, flip, imwrite

baseDir = "./colorferet/cropped_straight/"

for img in os.listdir(baseDir):

        image = imread(baseDir + img)
        imgFlipped = flip(image, 1)
        imwrite(baseDir + img[:-3] + '_mirror' + '.jpg', imgFlipped)
