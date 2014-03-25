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
  #cv2.imshow('mask',edges)
  biggest =None
  max_area = 0
  #blk = cv2.bitwise_not(grey)
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
  res = cv2.morphologyEx(edges,cv2.MORPH_OPEN,kernel)
  ret,thresh = cv2.threshold(edges,127,255,0)
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
    cv2.fillPoly(edges, [cnt], (100,20,90), 4)
    cv2.fillPoly(dest, [cnt], (255,255,255), 4)

    x = cv2.cvtColor(dest,cv2.COLOR_GRAY2RGB)
    cv2.putText(x, ">|<", (600,400), cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255), thickness=1)
    cv2.imshow('contour-highlighted image.jpg', x)

while 1:
  main()
  cv2.waitKey(27)

