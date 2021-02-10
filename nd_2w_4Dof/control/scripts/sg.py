#!/usr/bin/env python

import sys
import math
import rospy
from moveit_commander import RobotCommander, roscpp_initialize, roscpp_shutdown
from moveit_msgs.msg import RobotState, Constraints
from geometry_msgs.msg import Pose


if __name__ == '__main__':
    roscpp_initialize(sys.argv)
    rospy.init_node('moveit_py_demo', anonymous=True)
    
    robot = RobotCommander()
    rospy.sleep(1)
    
    m = robot.arm

    # move init
    m.set_pose_target([0.1, 0.0, 0.2,  math.pi, 0, 0])
    m.go()
    
    # move y
    m.set_pose_target([0.0,-0.1, 0.2,  math.pi, 0, 0])
    m.go()

    # move z
    m.set_pose_target([0.1,-0.1, 0.2,  math.pi, 0, 0])    
    m.go()
 
    # rotate z
    m.set_pose_target([0.1,-0.1, 0.2,  math.pi, 0, math.pi/2])
    m.go()
