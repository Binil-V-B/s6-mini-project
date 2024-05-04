# used to take a image of the parking area which can be used for mapping the rectangles

import cv2

cap = cv2.VideoCapture(1)
ret,frame = cap.read()

try:
    cv2.imwrite("screenshot.png",frame)
    print("Screenshot was succesfully captured")
except:
    print("screenshot not captured")

