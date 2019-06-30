import os

#the cleaning was not done perfectly. run this script to see all the values each of the attributes can take,
#so that such values can be dealt with expression as target:
    pass
baseDir = '/home/tejvi/Documents/colorferet/labels0/'

features = set()
count = 0
for file in os.listdir(baseDir):
    print(count)
    count += 1
    text = open(baseDir + file, 'r')
    for line in text.readlines()[6:]:
        features.add(line)
    text.close()

print(features)
