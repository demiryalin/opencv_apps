#!/usr/bin/python3

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Camera():
    def __init__(self):
        rospy.init_node("camera_node")
        self.bridge = CvBridge()
        rospy.Subscriber("camera/rgb/image_raw", Image, self.CameraCallback)
        rospy.spin()

    def CameraCallback(self, image_data):
        img = self.bridge.imgmsg_to_cv2(image_data, "bgr8")
        # b,g,r = cv2.split(img)
        # img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # img4 = cv2.merge((b,g,r))
        # cv2.imshow("robot head camera", img)
        # cv2.imshow("B", b)
        # cv2.imshow("G", g)
        # cv2.imshow("R", r)
        # cv2.imshow("merged image", img4)
        # cv2.imshow("robot head camera gray", img2)
        # cv2.imshow("robot head camera hsv", img3)
        cv2.waitKey(1)

Camera()