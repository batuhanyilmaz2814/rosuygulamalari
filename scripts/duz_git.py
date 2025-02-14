#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Bu uygulama robotun tek eksende hareket etmesini sağlamaktadır.
"""

import rospy
from geometry_msgs.msg import Twist

def hareket():  #Ana fonksiyonumuzu yazıyoruz.
    rospy.init_node("duz_git_node", anonymous=True) #Node'unumuz tanımladık.
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10) #Robotun hareketini sağlayan topic'i tanımladık.
    hiz_mesaji = Twist() #Hız mesajı oluşturduk.
    hiz_mesaji.linear.x = 0.7 #Robotun ileri yönde hareket etmesini sağladık.
    mesafe = 5 #Robotun gideceği mesafeyi belirledik.

    yer_degistirme = 0
    t0 = rospy.Time.now().to_sec() #Başlangıç zamanını aldık.

    while(yer_degistirme < mesafe): #Robotun heaket etmesi için bir döngü yazdık.
        pub.publish(hiz_mesaji) #Hız mesajını yayımladık.
        t1 = rospy.Time.now().to_sec() #Anlık zamanı aldık.
        yer_degistirme = hiz_mesaji.linear.x * (t1-t0) #Yer değiştirmeyi güncelledik.

    hiz_mesaji.linear.x = 0 #Robotun durmasını sağladık.
    pub.publish(hiz_mesaji) #Hız mesajını yayımladık.
    rospy.loginfo("Hedefe ulaşildi!")



hareket() #Ana fonksiyonumuzu çağırdık.     

