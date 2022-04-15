#!/usr/bin/env python

import rospy
import tf
import math
from std_msgs.msg import Float32
from nav_msgs.msg import Odometry

class distance:
    def __init__(self):
        rospy.init_node("pub_distance")
        rospy.Subscriber("odom",Odometry,self.callback)
        self.x = 0
        self.y = 0
        rospy.spin()

    def callback(self,data):
        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y
        dist = (self.x**2 + self.y**2)**0.5
        print("distance = {0} x = {1} y = {2}".format(dist,self.x,self.y))

if __name__ == "__main__":
    d = distance()