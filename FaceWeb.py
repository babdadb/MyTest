import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0) #(0) - веб камера
haar_cascade=cv.CascadeClassifier('haar_face.xml')


while True:
     isTrue, frame = capture.read()
     gray=cv.cvtColor(frame,10)

     faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10)
     for (x,y,w,h) in faces_rect:
         cv.rectangle(frame, (x+w//4,y+h//4), (x+3*w//4,y+3*h//4), (0,255,0), thickness=2)

     cv.imshow('Vid',frame)

     if cv.waitKey(20) & 0xFF==ord('d'):
         break

capture.release()
cv.destroyAllWindows()