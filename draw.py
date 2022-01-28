import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
# 1. Paint certain colour

#blank[200:300,300:400]=0,0,255
#cv.imshow('blank',blank)


# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[1]//2), (0,255,0), thickness=-1)
# cv.imshow('blank',blank)

#cv.circle(blank, (blank.shape[1]//2,blank.shape[1]//2), 50, (0,255,0), thickness=1)
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('blank',blank)
cv.waitKey(0)