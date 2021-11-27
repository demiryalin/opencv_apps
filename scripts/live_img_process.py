#!/usr/bin/python3
from contextlib import redirect_stderr

import rospy
import cv2
import numpy as np
#
# blue = np.uint8([[[255, 0, 0]]])
# hsv = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
cap = cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    img = cv2.resize(img, (640, 480))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    min_blue = np.array([110,100,100])
    max_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, min_blue, max_blue)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Orijinal", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
