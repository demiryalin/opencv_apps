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
        cv2.line(img,(0,0),(250,250),(255,0,0),thickness=5)
        cv2.rectangle(img,(250, 175),(500,125),(123,23,200),thickness=3)
        cv2.circle(img,(100,100),10, (0,0,255), -1)
        cv2.putText(img, "ROS", (0,150),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255),2)
        cv2.imshow("img",img)
        cv2.waitKey(1)

Camera()