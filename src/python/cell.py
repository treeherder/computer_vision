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
  ret,thresh = cv2.threshold(blk,127,255,0)
  contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
  dest = np.zeros(thresh.shape, np.uint8)
  print contours[1:]
  print len(contours)
  print hierarchy
  for cnt in contours[1:]:
    if cnt.any() in hierarchy[0][1:]:
      rect  = cv2.minAreaRect(cnt)
      points = cv2.cv.BoxPoints(rect)
      points  = np.int0(np.around(points))
      cv2.drawContours(dest, [cnt],0,(0,255,0),2)
      cv2.polylines(dest, [points], True,( 255,255,255), 2 )
    cv2.imshow('contour-highlighted image.jpg', dest)
    cv2.imwrite("../images/bound.jpg", dest)
    cv2.imshow('edges', thresh)
if __name__ == '__main__':
  mask(frame)	
  if cv2.waitKey(0) & 0xff == 27:  #escape
    cv2.destroyAllWindows()