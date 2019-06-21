import os

#

imgDir = "./colorferet/cropped_straight/"
baseDir1 = "./colorferet/dvd1/data/ground_truths/name_value/"
baseDir2 = "./colorferet/dvd2/data/ground_truths/name_value/"
writeDir = "./colorferet/labels0/"
wmode = "w"

c = 0

for imgName in os.listdir(imgDir):
    dir = baseDir1
    try:

        if int(imgName[:5]) >= 740:
            dir = baseDir2

        wFile = open(writeDir + imgName[:-3] + 'txt', wmode)
        file1 = open(dir + imgName[:5] + '/' + imgName[:5] + '.txt', "r")
        file2 = open(dir + imgName[:5] + '/' + imgName[:-3] + 'txt', "r")

        [wFile.write(line) for line in file1.readlines()[1:]]
        [wFile.write(line) for line in file2.readlines()[13:16]]   #idk why these indices, doesnt work otherwise

        wFile.close()
        file1.close()
        file2.close()

        print(c)
        c += 1

    except:
        print(imgName, "FAILED")
