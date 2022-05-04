#!/usr/bin/env python

import rospy

from std_msgs.msg import String


class goalreached():
    def __init__(self):
        rospy.init_node("goal_reache_node")
        rospy.Subscriber("goal_reached",String,self.callback)
        rospy.spin()

    def callback(self,data):
        rospy.loginfo(data.data)



a = goalreached()
