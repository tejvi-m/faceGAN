import cv2 as cv
import numpy as np
import os



baseDir = './colorferet/straightened/'
destDir = './colorferet/cropped_straight/'
c = 0

face_cascade = cv.CascadeClassifier('./pretrainedModels/haarcascade_frontalface_default.xml')

for image in os.listdir(baseDir):
    targImg = baseDir + image
    img = cv.imread(targImg)
    print(targImg, c)
    c += 1
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    try:
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:

            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y - 90 : y + h + 50, x - 30 : x + w + 30]

        targaddr = destDir + image
        cv.imwrite(targaddr, roi_color)
        
    except Exception as e:
        print(e, image, "FAILED")
