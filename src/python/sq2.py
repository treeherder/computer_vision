import cv2
import numpy as np


def find_cell(img):
    squares = []
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray", gray)

    gaussian = cv2.GaussianBlur(gray, (5, 5), 0)

    temp,bin = cv2.threshold(gaussian, 80, 255, cv2.THRESH_BINARY)
    # cv2.imshow("bin", bin)

    contours, hierarchy = cv2.findContours(bin, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours( gray, contours, -1, (0, 255, 0), 3 )

    #cv2.imshow('contours', gray)
    for cnt in contours:
        cnt_len = cv2.arcLength(cnt, True)
        cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
        if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
            cnt = cnt.reshape(-1, 2)
            max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
            if max_cos < 0.1:
                squares.append(cnt)
    return squares

if __name__ == '__main__':
    img = cv2.imread('/projects/cv/images/t-img2.jpg')

    #cv2.imshow("origin", img)

    squares = find_squares(img)  
    print "Find %d squres" % len(squares)
    cv2.drawContours( img, squares, -1, (0, 255, 0), 3 )
    cv2.imshow('squares', img)

    cv2.waitKey()