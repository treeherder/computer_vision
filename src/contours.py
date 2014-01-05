import numpy as np
import cv2


def cntr(img):

  ret,thresh = cv2.threshold(img,127,255,1)
  contours,h = cv2.findContours(thresh,1,2)
  for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print (len(approx))
    if len(approx)==5:
      print ("pentagon")
      cv2.drawContours(img,[cnt],0,255,-1)
    elif len(approx)==3:
      print ("triangle")
      cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
      print ("square")
      cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    elif len(approx) == 9:
      print ("half-circle")
      cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
      print ("circle")
      cv2.drawContours(img,[cnt],0,(0,255,255),-1)
 
  return(img)