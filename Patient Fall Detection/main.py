# Fall detector main
# Kim Salmi, kim.salmi(at)iki(dot)fi
# http://tunn.us/arduino/falldetector.php
# License: GPLv3

import video
import time
import sys
import numpy as np
import cv2
import time


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

video = video.Video()
time.sleep(1.0) # let camera autofocus + autosaturation settle
video.nextFrame()
video.testBackgroundFrame()

while 1:
	video.nextFrame()
	video.testBackgroundFrame()
	video.updateBackground()
	video.compare()
	video.showFrame()
	video.testSettings()
	if video.testDestroy():
		sys.exit()


# Release everything if job is finished
#video.release()
#out.release()  #save video
#cv2.destroyAllWindows()