import cv2
import cvzone
import pickle
import numpy as np

width = 105
height = 48

cap=cv2.VideoCapture(1) # use 1 for using the input from the irius camera

with open("car_positions",'rb') as f:
    posList=pickle.load(f)

def checkParkingSpaces(imgpro):
    for pos in posList:
        x,y=pos


        imgCrop=imgpro[y:y+height,x:x+width]
       # cv2.imshow(str(x*y),imgCrop)
        count=cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img,str(count),(x,y+height-5),scale=1.5,thickness=2,offset=0) #used to display the text on the feed
        if count<600:# when the no of pixels in a crop area is low, there might not be a car present there
            colour=(0,255,0)
        else:
            colour=(0,0,255)
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), colour, 2)

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0) # used to loop the input video, not required when using camera
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    # imgBlur2 = cv2.GaussianBlur(imgGray,(5,5),10)
    imgThershold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThershold,5)
    kernal = np.ones((3,3),np.uint8)
    imgDilate = cv2.dilate(imgMedian,kernal,iterations=1)

    checkParkingSpaces(imgMedian)



    cv2.imshow("video",img)
    # cv2.imshow("imgblur",imgBlur)
    # cv2.imshow("afterdialate",imgMedian)
    # # cv2.imshow("imggray2",imgBlur2)
    # cv2.imshow("imgthresh",imgThershold)
    cv2.waitKey(10)