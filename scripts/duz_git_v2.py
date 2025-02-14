#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Bu uygulama robotun tek eksende hareket etmesini sağlamaktadır.
V2 Subscriber ve Publisher'ın aynı anda kullanıldığı versiyon.

"""

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class HedefeGit():
    def __init__(self):
        rospy.init_node("duz_git_node", anonymous=True) #Node'unumuz tanımladık.
        self.hedef_konum = 5.0
        self.guncel_konum = 0.0
        self.hontrol = True
        rospy.Subscriber("odom", Odometry, self.odomCallback) #Robotun konumunu aldığımız topic'i tanımladık.
        pub = rospy.Publisher("cmd_vel",Twist,queue_size=10) #Robotun hareketini sağlayan topic'i tanımladık.
        rate = rospy.Rate(10) #Node'un 1Hz'de çalışmasını sağladık.
        while not rospy.is_shutdown():
            if self.hontrol:
                hiz_mesaji = Twist()
                hiz_mesaji.linear.x = 0.7
                pub.publish(hiz_mesaji)
            else:
                hiz_mesaji = Twist()
                hiz_mesaji.linear.x = 0
                pub.publish(hiz_mesaji)
                rospy.loginfo("hedefe varildi")
            rate.sleep( )
    def odomCallback(self, mesaj): #Robotun konumunu aldığımız fonksiyonumuzu yazıyoruz.
        print(mesaj.pose.pose.position.x) #Robotun x konumunu ekrana yazdırıyoruz.
        self.guncel_konum = mesaj.pose.pose.position.x #Robotun x konumunu güncelliyoruz.
        rospy.sleep(1) #1 saniye bekliyoruz.
        if self.guncel_konum <= self.hedef_konum: #Eğer robotun konumu hedef konumdan küçükse:
            self.hontrol = True
        else:
            self.hontrol = False


HedefeGit() #Ana fonksiyonumuzu çağırdık.