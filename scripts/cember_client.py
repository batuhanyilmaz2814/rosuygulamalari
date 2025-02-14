#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Çember hareketi - istemci kismi
"""

import rospy
from basic_examples.srv import CemberHareket

rospy.wait_for_service("cember_servis")
try:
    yaricap = float(input("Yaricap degerini giriniz:"))
    servis = rospy.ServiceProxy("cember_servis", CemberHareket)
    servis(yaricap)
except rospy.ServiceException:
    print("Servis çağrısı başarısız oldu")