import cv2
import numpy as np
import contours as ors
c = cv2.VideoCapture(0)

def main():
  ret,img = c.read() 
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

while 1:
  main()
  cv2.waitKey(27)

