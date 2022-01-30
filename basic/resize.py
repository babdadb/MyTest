import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    # any frames
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)    

    dimensions=(width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes (width,height):
    # Live Video only
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Videos/dog.mp4') #(0) - веб камера

while True:
    isTrue, frame = capture.read()
    
    frame_resized=rescaleFrame(frame)
    
    cv.imshow('Vid',frame)
    cv.imshow('VidResized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()