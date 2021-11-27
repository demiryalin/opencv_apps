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
        red_img = cv2.imread("kirmizi.png")
        height, width, _ = img.shape
        new_red_img = cv2.resize(red_img, (width, height))
        #addedimg = cv2.add(img, new_red_img)
        addedimg = cv2.addWeighted(img, 0.8, new_red_img, 0.2, 0)
        subtr = cv2.subtract(img, new_red_img)
        subtr2 = cv2.subtract(new_red_img, img)
        cv2.imshow("added image", addedimg)
        cv2.imshow("subtr image", subtr)
        cv2.imshow("subtr image2", subtr2)
        cv2.waitKey(1)

Camera()