from dlibLandmarks import dlibLandmarks
import cv2
import os

baseDir = './colorferet/dec_jpg/'
saveDir = './colorferet/straightened/'

#only relevant coordinates
noseCoordinates = [28, 29, 30, 31]
chinCoordinate = [9]

c = 0

straightenedImgs = os.listdir(saveDir)
for imgFile in os.listdir(baseDir):

    try:
        if imgFile not in straightenedImgs:
            img = dlibLandmarks(image = baseDir + imgFile, resize = False, relevantCoords = noseCoordinates ,
                                        show = False, save = True, savePath = saveDir + imgFile)

            angle = img.angle
            if angle < 0:
                angle *= -1
            if (angle >= 1.61443) or (angle <= 1.527163):
                straightenedImage = img.straighten()
            else:
                cv2.imwrite(saveDir + imgFile, cv2.imread(baseDir + imgFile))

            print(c)
            c += 1
    except:
        print("failed", imgFile)
