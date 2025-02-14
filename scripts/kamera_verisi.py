#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Kameradan gelen veriyi okuma
"""

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class RobotKamera():
    def __init__(self):
        rospy.init_node("kamera")
        rospy.Subscriber("camera/image_raw", Image, self.kameraCallback)
        self.bridge = CvBridge()
        rospy.spin()

    def kameraCallback(self, image):
        self.foto = self.bridge.imgmsg_to_cv2(image, "bgr8")
        cv2.imshow("Kamera", self.foto)
        cv2.waitKey(1)

nesne = RobotKamera()
