from collections import OrderedDict
import numpy as np
import cv2
import math
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
from scipy.misc import imread, imshow, imsave
from scipy import ndimage

FACIAL_LANDMARKS_IDXS = OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
	("nose", (27, 36)),
	("jaw", (0, 17))
])


#Does dlib work on "horizontal" faces???
#gives the four "corners" of the relevant rectangle
def rect_to_bb(rect):
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y

	return (x, y, w, h)

#predictor returns "shape". converting that to a numpy array? of tuples
def shape_to_np(shape, dtype="int"):
	coords = np.zeros((68, 2), dtype=dtype)

	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)

	return coords

class dlibLandmarks:
	def __init__(self, resize = True, image, relevantCoords = list(range(1, 69)), face = False, show = False, save = True,
	savePath = 'landmarkedFace0.jpg', color = (0, 0, 255), size = 3):
		self.imgPath = image
		img = cv2.imread(image)
		if resize:
			self.image = imutils.resize(img, width = 500)
		else:
			self.image = img
		self.show = show
		self.save = save
		self.color = (0, 0, 255)
		self.size = 2
		self.face = face
		self.savePath = savePath
		self.coords = relevantCoords

	#line drawinf: for my reference or does it do anything at all
	def drawLine(self, array = None):

		#arrray doesn't need to be passed
		if array == None:
			array = self.LandmarkCoordinates
		#print(array)

		#Only care about the ycoords, because only looking for the highest and lowest points
		#Will fail if the image is rotated by 90 degrees? Then what?
		yCoords = [];
		for i in array:
			yCoords.append(i[1])
		yHighest = max(yCoords)
		yLowest = min(yCoords)
		#print(yHighest)

		highest = 0;
		lowest = 0;
		for (x, y) in array:
			if y == yHighest:
				highest = (x, y)
			else:
				pass
			if y == yLowest:
				lowest = (x, y)
			else:
				pass
		#print(highest, lowest)

		#will fail if people have naturally slant noses

		#img = cv2.line(self.image, highest, lowest, (255, 0, 0), thickness = 1)

		#cv2.imshow('output', img)
		#cv2.waitKey(0)
		return (highest, lowest)

	def straighten(self):
		image = imread(self.imgPath)
		if self.angle > 0:
			imageRotated = ndimage.rotate(image, - 90 + self.angle * 180 / 3.14)
		else:
			imageRotated = ndimage.rotate(image, 90 + self.angle * 180 / 3.14)

		imsave(self.savePath, imageRotated)
		#print("img saved")
		#imshow(imageRotated)


	@property
	def angle(self):
		#wrt to the horizontal
		(x1, y1), (x2, y2) = self.drawLine(self.LandmarkCoordinates)

		if (x1 == x2):
			return 3.14 / 2
		slope = (y2 - y1) / (x2 - x1)

		angle = math.atan(slope)
		#print(angle)

		return angle

	@property
	def LandmarkCoordinates(self):

		detector = dlib.get_frontal_face_detector()
		predictor = dlib.shape_predictor('./pretrainedModels/shape_predictor_68_face_landmarks.dat')

		gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
		rects = detector(gray, 1)

		for (i, rect) in enumerate(rects):

			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)

			(x, y, w, h) = face_utils.rect_to_bb(rect)
			#if self.face:
				#cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 255, 0), 2)

			#if self.show or self.save:
				#index = 1
				#for (x, y) in shape:
			#		if index in self.coords:
			#			cv2.circle(self.image, (x, y), self.size, self.color, -1)
			#		index += 1

		if self.save:
			cv2.imwrite(self.savePath, self.image)

		if self.show:
			cv2.imshow("Output", self.image)
			cv2.waitKey(0)

		requiredCoords = []
		for i in self.coords:
			requiredCoords.append((shape[i - 1]).tolist())
		#print(requiredCoords)
		return requiredCoords


#write a fucntion for triangulation???
#if __name__ == "__main__":
