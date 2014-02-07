import cv2
import numpy as np
import contours as ors
import argparse

parser = argparse.ArgumentParser(description = "performs canny edge detection on a still image")
parser.add_argument("image", help = "give the name of a file in ../images/", type=str)
args = parser.parse_args()

def threshold(z):
  img = cv2.imread("../images/{0}".format(z))
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  (hue, sat, val)  = cv2.split(hsv)
  hf, hue  = cv2.threshold(hue, 255, 255, cv2.THRESH_BINARY)   #0,20
  sf, sat  = cv2.threshold(sat, 255, 255, cv2.THRESH_BINARY)   #0,20
  vf, val  = cv2.threshold(val, 10, 255, cv2.THRESH_BINARY)  #30,45
  mrgd = cv2.merge([hue, sat, val])    #threshold for just the black square
  bgr = cv2.cvtColor(mrgd, cv2.COLOR_HSV2BGR)
  gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (5,5), 0)
  mask = ors.cntr(gray)
  edges = cv2.Canny(mask,100,200)
  cv2.imshow('mask',edges)
  cv2.imshow('hue',hue)
  cv2.imshow('sat',sat)
  cv2.imshow('val',val)

  cv2.imwrite("../images/t-{0}".format(z), edges)
  if cv2.waitKey(0) & 0xff == 27:  #escape
    cv2.destroyAllWindows()

threshold(args.image)