import cv2
cap = cv2.VideoCapture("test.avi")
cv2.namedWindow("test", cv2.WINDOW_AUTOSIZE)
while(True):
    f, img = cap.read()
    cv2.imshow("test", img)
    cv2.waitKey(1)