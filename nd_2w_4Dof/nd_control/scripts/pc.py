#!/usr/bin/env python
import rospy
import pcl
import numpy as np
import ctypes
import struct
import sensor_msgs.point_cloud2 as pc2

from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header
from random import randint
from roslib import message

#rospy.init_node('listen', anonymous=True)
#rospy.Subscriber("mybot/camera1/depth/points", PointCloud2, callback_kinect)
    
points_list = []

for data in pc2.read_points(ros_cloud, skip_nans=True):
    points_list.append([data[0], data[1], data[2], data[3]])

pcl_data = pcl.PointCloud_PointXYZRGB()
pcl_data.from_list(points_list)

print(points_list)