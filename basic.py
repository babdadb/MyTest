import cv2 as cv

img=cv.imread('Photos/group 1.jpg')
cv.imshow('Basic',img)


#img=cv.cvtColor(img,10)
img=cv.GaussianBlur(img,(2 ,2),cv.BORDER_DEFAULT)
#cv.imshow('Blur',img)

img=cv.Canny(img,125,175)
cv.imshow('Canny',img)

img=cv.dilate(img,(3,3),iterations=2)
cv.imshow('Diated',img)

img=cv.erode(img,(3,3))
cv.imshow('Fin',img) 


cv.waitKey(0)