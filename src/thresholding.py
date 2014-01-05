import cv2
import numpy as np

def threshold(z):
  img = cv2.imread("../images/{0}".format(z))
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  (hue, sat, val)  = cv2.split(hsv)
  hf, hue  = cv2.threshold(hue, 0, 20, cv2.THRESH_BINARY)
  sf, sat  = cv2.threshold(sat, 0, 20, cv2.THRESH_BINARY)
  vf, val  = cv2.threshold(val, 30, 45, cv2.THRESH_BINARY)
  mrgd = cv2.merge([hue, sat, val])
  bgr = cv2.cvtColor(mrgd, cv2.COLOR_HSV2BGR)
  gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
  cv2.imwrite("../images/t-{0}".format(z), gray)
  cv2.imshow('gray', gray)
  cv2.imshow('bgr ', bgr)
  
  if cv2.waitKey(0) & 0xff == 27:  #escape
    cv2.destroyAllWindows()
threshold('img2.jpg')