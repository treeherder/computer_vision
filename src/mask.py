import cv2
import numpy as np

while True:
    frame = cv2.imread('/projects/cv/images/t-img1.jpg')

    frame = cv2.blur(frame,(3,3))
    
    # convert to hsv and find range of colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((0, 80, 80)), np.array((20, 255, 255)))
    thresh2 = thresh.copy()
    
    # find contours in the threshold image
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    # finding contour with maximum area and store it as best_cnt
    max_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt
    
    # finding centroids of best_cnt and draw a circle there
    M = cv2.moments(best_cnt)
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    cv2.square(frame,(cx,cy),5,255,-1)
    cv2.imshow("video", frame)
    if cv2.waitKey(5)==27:   #press esc to exit
        break
        cv2.destroyAllWindows()