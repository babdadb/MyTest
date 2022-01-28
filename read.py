from turtle import width
import cv2 as cv
from numpy import true_divide

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('cat',   img)

def rescaleFrame(frame,scale=0.75):
    width=frame.shape[1]*scale
    height=frame.shape[0]*scale
    dimensions=(width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

cv.waitKey(4000)

# capture = cv.VideoCapture('Videos/dog.mp4') #(0) - веб камера
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Vid',frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()