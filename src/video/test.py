import cv2
import numpy as np

capture = cv2.VideoCapture(0)
flag, frame = capture.read()
width = np.size(frame, 1) # automatically determine frame dimensions
height = np.size(frame, 0)
print(width, height)
writer = cv2.VideoWriter(filename="test.mov", fourcc=cv2.cv.CV_FOURCC("R", "P", "Z", "A"),fps=24, frameSize=(width, height))   # .avi fourcc

while True:
  flag, frame = capture.read() # flag == 0 fails
  writer.write(frame) #write to the video file
  if flag == 0: # end of file
    break  
