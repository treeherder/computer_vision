import cv2
import numpy as np
c = cv2.VideoCapture("test.avi")

def main():
  ret,frame = c.read()
  cv2.imshow('frames',frame)
while True:
   main()
   if cv2.waitKey(5)==27:   #press esc to exit  
     break
     cv2.destroyAllWindows()
