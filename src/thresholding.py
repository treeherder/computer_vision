import cv2
import numpy as np
import contours as ors
def threshold(z):
  img = cv2.imread("../images/{0}".format(z))
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  (hue, sat, val)  = cv2.split(hsv)
  hf, hue  = cv2.threshold(hue, 0, 255, cv2.THRESH_BINARY)   #0,20
  sf, sat  = cv2.threshold(sat, 220, 255, cv2.THRESH_BINARY)   #0,20
  vf, val  = cv2.threshold(val, 45, 255, cv2.THRESH_BINARY)  #30,45
  mrgd = cv2.merge([hue, sat, val])    #threshold for just the black square
  bgr = cv2.cvtColor(mrgd, cv2.COLOR_HSV2BGR)
  gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
  cv2.imwrite("../images/t-{0}".format(z), gray)
  mask = ors.cntr(gray)
  cv2.imshow('mask', mask)
  if cv2.waitKey(0) & 0xff == 27:  #escape
    cv2.destroyAllWindows()

threshold('img2.jpg')