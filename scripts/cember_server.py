#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Çember hareketi - sunucu kısmı
"""

import rospy
from geometry_msgs.msg import Twist
from basic_examples.srv import CemberHareket

def cemberFonksiyonu(istek):
    hiz_mesaji = Twist()
    lineer_hiz = 0.4
    hiz_mesaji.linear.x = lineer_hiz
    yaricap = istek.yaricap
    # w = v/r
    hiz_mesaji.angular.z = lineer_hiz / yaricap
    while not rospy.is_shutdown():
        pub.publish(hiz_mesaji)


rospy.init_node("cember_hareket") # Node ismi

pub = rospy.Publisher("cmd_vel", Twist, queue_size=10) # Hareket komutu yayını
rospy.Service("cember_servis", CemberHareket, cemberFonksiyonu)
rospy.spin()