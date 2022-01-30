from tokenize import blank_re
import cv2 as cv
import numpy as np

img=cv.imread('Photos/cats.jpg')
cv.imshow('Basic',img)

blank = np.zeros(img.shape,dtype='uint8')

gray=cv.cvtColor(img,10)

#blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#canny=cv.Canny(blur,125,175)
#cv.imshow('Canny',canny)

ret,tresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
contours, hiearchies = cv.findContours(tresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

cv.imshow('Fin',tresh)

cv.drawContours(blank,contours,-1,(0,255,0),1)
cv.imshow('Fin',blank)

#print(f'{len(contours)} contour(s) found')
cv.waitKey(0)