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
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, maske = cv2.threshold(gray_img, 50, 255, cv2.THRESH_BINARY_INV)
        and_is = cv2.bitwise_and(img, img, mask=maske)
        cv2.imshow("robot head camera", and_is)
        cv2.waitKey(1)

Camera()