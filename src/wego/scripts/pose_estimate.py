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
        self.current_quaternion_x = None
        self.current_quaternion_y = None
        self.current_quaternion_z = None
        self.current_quaternion_w = None
        self.pos = None


        self.pos = PoseWithCovarianceStamped()
        # self.listener =tf.TransformListener()
        
        self.seq = None

        self.cmd_pub = rospy.Publisher("cmd_vel",Twist,queue_size=1)
        self.pub = rospy.Publisher("/move_base_simple/goal",PoseStamped,queue_size = 10)
        self.pose_pub = rospy.Publisher("/initialpose",PoseWithCovarianceStamped,queue_size = 10)
        rospy.Subscriber("/odom",Odometry,self.pose_setting_callback)
        rospy.Subscriber("/amcl_pose",PoseWithCovarianceStamped,self.quaternion_callback)
        rospy.Subscriber("cmd_vel",Twist,self.cmd_vel_callback)
        rospy.spin()


## my pose -> amcl_pose
    def cmd_vel_callback(self,cmd_data):

        self.vel_x = cmd_data.linear.x
        self.vel_yaw = cmd_data.angular.z

    def quaternion_callback(self,data):

        self.seq = data.header.seq
        self.current_quaternion_x = data.pose.pose.orientation.x
        self.current_quaternion_y = data.pose.pose.orientation.y
        self.current_quaternion_z = data.pose.pose.orientation.z
        self.current_quaternion_w = data.pose.pose.orientation.w
   

    def pose_setting_callback(self, data):

        rospy.loginfo("time")

        # base_link from map
        self.listener =tf.TransformListener()
        self.listener.waitForTransform('/base_link','/map',rospy.Time(0),rospy.Duration(1.0))
        (trans, rot )= self.listener.lookupTransform('/map','/base_link',rospy.Time(0))
        self.current_x = trans[0]
        self.current_y = trans[1]
        # self.current_quaternion_x = rot[0]
        # self.current_quaternion_y = rot[1]
        # self.current_quaternion_z = rot[2]
        # self.current_quaternion_w = rot[3]


        # pose update
        self.pos.header.seq = self.seq
        self.pos.header.stamp = rospy.Time.now()
        self.pos.header.frame_id = "map"
        self.pos.pose.pose.position.x = self.current_x
        self.pos.pose.pose.position.y = self.current_y
        self.pos.pose.pose.orientation.x = self.current_quaternion_x
        self.pos.pose.pose.orientation.y = self.current_quaternion_y
        self.pos.pose.pose.orientation.z = self.current_quaternion_z
        self.pos.pose.pose.orientation.w =  self.current_quaternion_w
        self.pos.pose.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853892326654787]



        # goal point 
        goal_xy = [[1.2896 , -17.1],[1.5,-12.0],[3.1,-11.5],[5.31,-14.98],[-0.968,14.75],[-8.0,7.3],[-5.7,7.16],[-6.95,-1.0]]
        goal_quaternion = []



        # goal
        pub_data = PoseStamped()
        pub_data.header.stamp = rospy.Time.now()
        pub_data.header.frame_id = "map"
        pub_data.pose.position.x = goal_xy[self.count][0]
        pub_data.pose.position.y = goal_xy[self.count][1]
        pub_data.pose.orientation.x = 0
        pub_data.pose.orientation.y =  0
        pub_data.pose.orientation.z = self.current_quaternion_z
        pub_data.pose.orientation.w =  self.current_quaternion_w


        self.pub.publish(pub_data)

        # print 
        print("currnt x :{0} y: {1}".format(self.current_x, self.current_y))
        print("current_quaternion x = {0} y = {1}, z = {2}, w = {3}".format(self.current_quaternion_x,self.current_quaternion_y,self.current_quaternion_z,self.current_quaternion_w))
        print("goal_x distance :{0} goal_y distance : {1}".format(abs(self.current_x - goal_xy[self.count][0]),abs(self.current_y - goal_xy[self.count][1])))
        print("goal_x = {0} goal_y = {1}".format(goal_xy[self.count][0],goal_xy[self.count][1]))
        distance = ((self.current_x - goal_xy[self.count][0])**2 +(self.current_y - goal_xy[self.count][1])**2)**0.5
        # if abs(self.current_x - goal_xy[self.count][0]) < 1 and abs(self.current_y - goal_xy[self.count][1]) < 1:
        print("distance = {0}".format(distance))
        print("goal number : {0}".format(self.count+1))



        # mission 1

        if self.count == 0:
            if distance < 0.1:
                self.pose_pub.publish(self.pos)
                rospy.sleep(5.0)
                self.count += 1
        elif self.count == 1:
            if distance < 1.5:
                self.count += 1
        elif self.count == 2:
            if distance < 1.0:
                self.count += 1
        elif self.count == 3 :
            if distance < 0.1 and self.vel_x == 0:
                # self.pose_pub.publish(self.pos)
                rospy.sleep(5.0)
                self.count += 1
        elif self.count== 5:
            if distance < 1.0:
                self.count +=1
        else:
            if distance < 1.0:
                self.count += 1


        # initial pose update
        if ((self.current_x + 8.9)**2 + (self.current_y - 7.0)**2)**0.5 < 0.5:
            self.pose_pub.publish(self.pos)
            print("point1") 
            rospy.sleep(2.0)

        elif ((self.current_x + 3.8)**2 + (self.current_y + 1.0)**2)**0.5 < 0.5:
            self.pose_pub.publish(self.pos)
            print("point2")
            rospy.sleep(2.0)
        elif ((self.current_x - 1.0)**2 + (self.current_y + 6.5)**2)**0.5 < 0.5:
            self.pose_pub.publish(self.pos)
            print("point3")
            rospy.sleep(2.0)

        elif ((self.current_x - 1.3)**2 + (self.current_y + 14.0)**2)**0.5 < 0.5:
            # self.pose_pub.publish(self.pos)
            print("point4")
            rospy.sleep(2.0)

        elif ((self.current_x - 1.2)**2 + (self.current_y - 2.0)**2)**0.5 < 0.5:
            # self.pose_pub.publish(self.pos)
            print("point5")
            rospy.sleep(2.0)

        elif ((self.current_x - 1.25)**2 + (self.current_y - 9.0)**2)**0.5 < 0.5:
            # self.pose_pub.publish(self.pos)
            print("point6")
            self.count += 1
            rospy.sleep(2.0)

        elif ((self.current_x + 2.7)**2 + (self.current_y - 14.75)**2)**0.5 < 0.5:
            self.pose_pub.publish(self.pos)
            self.count += 1
            print("point7")
            rospy.sleep(2.0)

if __name__ =="__main__":
    a = Goal()

