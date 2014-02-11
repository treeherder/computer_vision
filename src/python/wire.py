import numpy as np
import cv2
from matplotlib import pyplot as plt
import argparse 
from wire_thresholding import threshold
import time
parser = argparse.ArgumentParser()
parser.add_argument("img", help = "give the name of a file in ../../images/", type=str)
args = parser.parse_args() 
threshold(args.img)
time.sleep(2)

frame = cv2.imread('../../images/t-{0}'.format(args.img))
orig  =  cv2.imread('../../images/{0}'.format(args.img))


def mask(img):
  biggest =None
  max_area = 0
  grey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
  #blk = cv2.bitwise_not(grey)
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
  res = cv2.morphologyEx(grey,cv2.MORPH_OPEN,kernel)
  ret,thresh = cv2.threshold(grey,127,255,0)
  contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
  dest = np.zeros(thresh.shape, np.uint8)
  print contours[::1]
  print len(contours)
  print hierarchy
  for cnt in contours[::1]:
    rect  = cv2.minAreaRect(cnt)
    points = cv2.cv.BoxPoints(rect)
    points  = np.int0(np.around(points))
    #cv2.drawContours(dest, [cnt],0,(0,255,0),2)
    #cv2.polylines(dest, [points], True,( 255,255,255), 2 )
    cv2.fillPoly(orig, [cnt], (100,20,90), 4)
    cv2.fillPoly(dest, [cnt], (255,255,255), 4)

    x = cv2.cvtColor(dest,cv2.COLOR_GRAY2RGB)
    cv2.imshow('contour-highlighted image.jpg', x)
    cv2.imwrite("../../images/bound.jpg", x)

    cv2.imshow('masked image', orig)
if __name__ == '__main__':
  mask(frame) 
  if cv2.waitKey(0) & 0xff == 27:  #escape
    cv2.destroyAllWindows()