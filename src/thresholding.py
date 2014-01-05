import cv2
import numpy as np

def threshold(z):
  img = cv2.imread("../images/{0}".format(z))
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  (hue, sat, val)  = cv2.split(hsv)
  hf, hue  = cv2.threshold(hue, 100, 127, cv2.THRESH_BINARY)
  sf, sat  = cv2.threshold(sat, 100, 127, cv2.THRESH_BINARY)
  vf, val  = cv2.threshold(val, 120, 157, cv2.THRESH_BINARY)
  mrgd = cv2.merge([hue, sat, val])
  bgr = cv2.cvtColor(mrgd, cv2.COLOR_HSV2BGR)
  gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
  cv2.imwrite("../images/t-{0}".format(z), gray)

threshold('img2.jpg')