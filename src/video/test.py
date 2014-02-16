import cv2
import numpy as np

capture = cv2.VideoCapture(0)
flag, frame = capture.read()
width = np.size(frame, 1) # automatically determine frame dimensions
height = np.size(frame, 0)
writer = cv2.VideoWriter(filename="test.avi", fourcc=cv2.cv.CV_FOURCC('I', 'Y', 'U', 'V'),fps=15, frameSize=(width, height))   # .avi fourcc

while True:
  flag, frame = capture.read() # flag == 0 fails
  if flag == 0: # end of file
    break
  x = width/2
  y = height/2
  text_color = (255,0,0) # B,G,R
  cv2.putText(frame, "test", (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
  writer.write(frame) #write to the video file