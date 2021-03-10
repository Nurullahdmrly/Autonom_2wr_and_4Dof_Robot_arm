#!/usr/bin/env python
#-*-coding: utf-8 -*-
 
import rospy
from sensor_msgs.msg import LaserScan
 
def func(veri):
    
    #adet = len(veri.ranges)
    #print 'bir taramada uretilen uzaklik verisi adeti:', adet
   

    bolgeler = {
        'sag':  min(min(veri.ranges[0:143]), 30),
        'on_sag': min(min(veri.ranges[144:287]), 30),
        'on':  min(min(veri.ranges[288:431]), 30),
        'on_sol':  min(min(veri.ranges[432:575]), 30),
        'sol':   min(min(veri.ranges[576:719]), 30)
    }

    print bolgeler
 
      
def durdur():
    
    rospy.loginfo('sonlandirildi!')

if __name__ == "__main__":

    rospy.init_node('lidar_veri',anonymous=True)
    
    rospy.loginfo('Sonlandirmak icin CTRL+C')
    rospy.on_shutdown(durdur)
    
    rospy.Subscriber('/mybot/laser/scan', LaserScan, func)
    rospy.spin()
