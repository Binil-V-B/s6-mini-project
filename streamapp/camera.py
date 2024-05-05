import cv2,os
import numpy as np
import pickle
import cvzone

width = 105
height = 48
with open("parking/car_positions",'rb') as f:
	posList=pickle.load(f)
	

class VideoCamera(object):
	def __init__(self):
		self.cap = cv2.VideoCapture(1)
		success,self.image = self.cap.read()

	
	def checkParkingSpaces(self,imgpro):
		for pos in posList:
			x,y=pos
			# success, img = self.cap.read()

			imgCrop=imgpro[y:y+height,x:x+width]
			# cv2.imshow(str(x*y),imgCrop)
			count=cv2.countNonZero(imgCrop)
			cvzone.putTextRect(self.image,str(count),(x,y+height-5),scale=1.5,thickness=2,offset=0) #used to display the text on the feed
			if count<600:# when the no of pixels in a crop area is low, there might not be a car present there
				colour=(0,255,0)
			else:
				colour=(0,0,255)
			cv2.rectangle(self.image, pos, (pos[0] + width, pos[1] + height), colour, 2)

	def __del__(self):
		self.cap.release()

	def get_frame(self):
		success,self.image = self.cap.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		imgGray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
		imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    	# imgBlur2 = cv2.GaussianBlur(imgGray,(5,5),10)
		imgThershold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV,25,16)
		imgMedian = cv2.medianBlur(imgThershold,5)
		kernal = np.ones((3,3),np.uint8)
		imgDilate = cv2.dilate(imgMedian,kernal,iterations=1)
		self.checkParkingSpaces(imgDilate)
		
		frame_flip = cv2.flip(self.image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()



