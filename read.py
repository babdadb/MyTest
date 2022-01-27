import cv2 as cv
from numpy import true_divide

# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('cat',   img)
#cv.waitKey(2000)

capture = cv.VideoCapture('Videos/dog.mp4') #(0) - веб камера
while True:
    isTrue, frame = capture.read()
    cv.imshow('Vid',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()