#Python 2

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

j=0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fgmask = fgbg.apply(gray)
    
        #Find contours
        _, contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            areas = []
            for contour in contours:
                ar = cv2.contourArea(contour)
                areas.append(ar)
        
        max_area = max(areas or [0])

        max_area_index = areas.index(max_area)

        cnt = contours[max_area_index]

        M = cv2.moments(cnt)
        
        x, y, w, h = cv2.boundingRect(cnt)

        cv2.drawContours(fgmask, [cnt], 0, (255,255,255), 3, maxLevel = 0)
        
        if h < w:
            j += 1
            
        if j > 10:
            print "FALL DETECTED"
            print j
            cv2.putText(frame, 'FALL DETECTED', (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 2)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

        if h > w:
            j = 0 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        
    else:
        break

# Release everything if job is finished
cap.release()
out.release()  #save video
cv2.destroyAllWindows()
