import numpy as np
import cv2
from matplotlib import pyplot as plt
import argparse 


parser = argparse.ArgumentParser()
parser.add_argument("img", help = "give the name of a file in ../images/", type=str)
args = parser.parse_args() 

frame = cv2.imread('../images/{0}'.format(args.img))

def mask(img):
  biggest =None
  max_area = 0
  grey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
  blk = cv2.bitwise_not(grey)
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
  res = cv2.morphologyEx(blk,cv2.MORPH_OPEN,kernel)
  ret,thresh = cv2.threshold(res,127,255,0)
  contours, hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
  for cnt in contours:
    area = cv2.contourArea(cnt)
    if area >62 and area <300000 :
      peri = cv2.arcLength(cnt, True)
      approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
      if area > max_area and len(approx)==4:
      	biggest = approx
      	max_area = area
      cv2.drawContours(res,[approx],0,(20,130,50),-1)
  cv2.imshow('contour-highlighted image.jpg', res )
  cv2.imshow('edges', blk)
if __name__ == '__main__':
  mask(frame)	
  if cv2.waitKey(0) & 0xff == 27:  #escape
    cv2.destroyAllWindows()