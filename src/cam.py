import cv2
import numpy as np
c = cv2.VideoCapture(0)

while(1):
  ret,frame = c.read()
  cv2.imshow('frames',frame)
  if cv2.waitKey(5)==27:   #press esc to exit  
    break
cv2.destroyAllWindows()