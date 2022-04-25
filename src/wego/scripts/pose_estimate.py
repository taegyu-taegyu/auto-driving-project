#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped,PoseWithCovarianceStamped ,Twist
from nav_msgs.msg import Odometry 
import tf

class Goal:
    def __init__(self):

        rospy.init_node("Goal")
        # self.goal_position_x = float(input())
        # self.goal_position_y = float(input())
        # self.goal_position_z = float(input())
        self.vel_x = 0
        self.vel_yaw = 0
        self.count = 0
        self.quaternion_x = None
        self.quaternion_y = None
        self.quaternion_z = None
        self.quaternion_w = None
        self.pos = None

        # self.listener =tf.TransformListener()
        
        self.seq = None


        self.pose_count = 1
        self.cmd_pub = rospy.Publisher("cmd_vel",Twist,queue_size=1)
        self.pub = rospy.Publisher("/move_base_simple/goal",PoseStamped,queue_size=10)
        self.pose_pub = rospy.Publisher("/initialpose",PoseWithCovarianceStamped,queue_size=1)
        rospy.Subscriber("/odom",Odometry,self.pose_callback)
        rospy.Subscriber("/amcl_pose",PoseWithCovarianceStamped,self.seq_callback)
        rospy.Subscriber("cmd_vel",Twist,self.cmd_vel_callback)
        rospy.Timer(rospy.Duration(3.0),self.callback)
        rospy.Timer(rospy.Duration(15.0),self.Posecallback)
        rospy.spin()

## my pose -> amcl_pose
    def cmd_vel_callback(self,cmd_data):
        self.vel_x = cmd_data.linear.x
        self.vel_yaw = cmd_data.angular.z
    def seq_callback(self,data):
        self.seq = data.header.seq
    def pose_callback(self, data):

        self.listener =tf.TransformListener()
        self.listener.waitForTransform('/base_link','/map',rospy.Time(0),rospy.Duration(4.0))
        (trans, rot )= self.listener.lookupTransform('/map','/base_link',rospy.Time(0))

        self.current_x = trans[0]
        self.current_y = trans[1]
        self.quaternion_x = rot[0]
        self.quaternion_y = rot[1]
        self.quaternion_z = rot[2]
        self.quaternion_w = rot[3]
        print(self.current_x , self.current_y)
    
    def Posecallback(self,data):        
        self.pos = PoseWithCovarianceStamped()
        self.pos.header.seq = self.seq

        self.pos.header.stamp = rospy.Time.now()
        self.pos.header.frame_id = "map"

        self.pos.pose.pose.position.x = self.current_x
        self.pos.pose.pose.position.y = self.current_y

        self.pos.pose.pose.orientation.x = self.quaternion_x
        self.pos.pose.pose.orientation.y = self.quaternion_y
        self.pos.pose.pose.orientation.z = self.quaternion_z
        self.pos.pose.pose.orientation.w =  self.quaternion_w
        print("initialized")
        self.pose_pub.publish(self.pos)

        # rospy.loginfo(self.pos)

    def callback(self,event):
        # print("okay")
        cmd_pub =Twist()
        pub_data = PoseStamped()
        # pub_data.header.seq = 1
        pub_data.header.stamp = rospy.Time.now()
        pub_data.header.frame_id = "map"
        pub_data.pose.orientation.x = self.quaternion_x
        pub_data.pose.orientation.y =  self.quaternion_y
        pub_data.pose.orientation.z = self.quaternion_z
        pub_data.pose.orientation.w =  self.quaternion_w

        goal_xy = [[-5.0 , 6.0],[1.35  ,-17.30],[5.0,-12.0],[1.5,14.5]]

        pub_data.pose.position.x = goal_xy[self.count][0]
        pub_data.pose.position.y = goal_xy[self.count][1]
        self.pub.publish(pub_data)
        # print("current speed x :{0} z : {1}".format(self.vel_x,self.vel_yaw))
        # print("current goal x : {0} y : {1}".format(goal_xy[self.count][0],goal_xy[self.count][1]))
        print("currnt x :{0} y: {1}".format(self.current_x, self.current_y))
        print("x distance :{0} y distance : {1}".format(abs(self.current_x - goal_xy[self.count][0]),abs(self.current_y - goal_xy[self.count][1])))
        distance = ((self.current_x - goal_xy[self.count][0])**2 +(self.current_y - goal_xy[self.count][1])**2)**0.5
        # if abs(self.current_x - goal_xy[self.count][0]) < 1 and abs(self.current_y - goal_xy[self.count][1]) < 1:
        print("distance = {}".format(distance))
        print("goal number : {}".format(self.count+1))
        # print()
        if distance < 0.1:
            self.count +=1
            self.pose_pub.publish(self.pos)
        if self.count == 7:
            self.count =0
  
if __name__ =="__main__":
    a = Goal()

