#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


class Velocity:

    def __init__(self):
        rospy.init_node("vel_node",anonymous=False)
        
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size=1)
        rospy.Timer(rospy.Duration(1.0),self.callback)
        rospy.loginfo("initialized")
        rospy.spin()
    def callback(self,event):
        pub_data = Twist()
        pub_data.linear.x = 1.0

        self.pub.publish(pub_data)

if __name__ == "__main__":
    Velocity()