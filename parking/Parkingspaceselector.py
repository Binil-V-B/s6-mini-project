import cv2
import pickle

img = cv2.imread("screenshot.png")

try: # check whether the car_positions file is available, if available load the posList
    with open('car_positions','rb') as f:
        posList=pickle.load(f)
except: # if car_positions is not present then an empty list is created
    posList=[]

width = 105
height = 48


def mouseClick(events, x, y, flags,args):
    if events == cv2.EVENT_LBUTTONDOWN:   # used to create a rectangle everytime we click on the windows
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:  # deletes the rectangle when right clicked.
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)

    with open('car_positions','wb') as f: # used to save the rectangle to a file
        pickle.dump(posList,f)


while True:
    img=cv2.imread("screenshot.png") # we are reloading the image everytime so that we are able to delete rectangle with right clicks
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height), (255, 0, 0), 2)
    cv2.imshow("image", img)
    cv2.setMouseCallback("image", mouseClick)
    cv2.waitKey(1)
