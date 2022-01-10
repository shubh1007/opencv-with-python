import cv2 as cv
import numpy as np
import time

def collage(img):
    collage = np.zeros(img.shape, dtype= "uint8")
    newwidth, newheight = img.shape[1]//2, img.shape[0]//2
    img = cv.resize(img, (newwidth, newheight))
    for i in range(2):
        for j in range(2):
            pos = [newheight*(i+1), newwidth*(j+1)]
            collage[i*newheight: pos[0], j*newwidth: pos[1]] = img
    return collage

width, height = 640, 640
capture = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter("./myVideo.avi", fourcc, 20.0, (width, height))
frames = 0
flag = 0
while True:
    success, img = capture.read()
    if(cv.waitKey(1) & 0xff == 27):
        break
    if(frames%60 == 0):
        flag += 1
    img = cv.flip(img, 1)
    img = cv.resize(img, (width, height))
    img = collage(img)
    output.write(img)
    cv.putText(img, str(frames), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 2)
    cv.imshow("Video", img)
    frames += 1

capture.release()
output.release()
cv.destroyAllWindows()