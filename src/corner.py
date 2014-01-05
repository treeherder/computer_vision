import numpy as np
import cv2
from matplotlib import pyplot as plt

frame = cv2.imread('../images/t-img2.jpg')
grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

grey = np.float32(grey)
har = cv2.cornerHarris(grey,2,3,0.04)
har = cv2.dilate(har,None)

# tweak this threshold for the dilated image
frame[har>0.01*har.max()]=[0,0,255]

cv2.imshow('har', frame)
if cv2.waitKey(0) & 0xff == 27:  #escape
    cv2.destroyAllWindows()