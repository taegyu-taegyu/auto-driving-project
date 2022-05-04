#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped,PoseWithCovarianceStamped ,Twist
from nav_msgs.msg import Odometry 
import tf
from std_msgs.msg import String

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
        self.goal_pub = rospy.Publisher("goal_reached",String,queue_size=10)
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
        goal_xy = [[1.4,11.2],[0.824962854385,-0.301981925964],[-5.86247592418,7.3302264351],[1.40595856748,11.2159350485],[-7.03,-0.94],[1.00,-13.5],[-0.29,-12.19],[-2.6,13.94],[1.49,-11.3],[4.23,-15.3]]

        # currnt x :1.49659313188 y: -11.3354747947 4rkddmlwkd dkv
        # currnt x :-5.69941851859 y: -1.2655211505 tkantlf dkvdp

        # currnt x :-5.86247592418 y: 7.3302264351  point 4


#     x: 0.824962
#     y: -0.30198



#         # currnt x :-5.69941851859 y: -1.2655211505 tkantlf dkvdp

#         currnt x :1.40595856748 y: 11.2159350485   

#         currnt x :0.492039823533 y: 11.1391706655 point2

#         currnt x :-2.50533688622 y: 14.938261851

#         currnt x :-2.67035945166 y: 13.9440043445 point1

#         currnt x :1.00357917739 y: -13.5033084975 ruddb1

#         currnt x :-0.139447018397 y: -13.4679528612 ruddb 2
        
#         currnt x :-0.29814386193 y: -12.1901362965 point 3


#     currnt x :-7.03884007968 y: -0.941910995744 point 5


# ^Ccurrnt x :4.23463068593 y: -15.3309724056 goal  point 









        # goal reached
        g_r = String()
        g_r.data = "goal_reached"



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



        # mission 2

        if self.count == 0:
            if distance < 0.1:
                self.goal_pub.publish(self.goal_pub)
                rospy.sleep(5.0)
                self.count += 1

        elif self.count == 1:
            if distance < 0.1:
                rospy.sleep(5.0)
                self.count += 1

        elif self.count == 2:

            if distance < 0.1:
                rospy.sleep(5.0)
                self.count += 1

        elif self.count == 3 :

            if distance < 0.1 and self.vel_yaw == 0:
                self.goal_pub.publish(self.goal_pub)
                rospy.sleep(5.0)
                self.count += 1

        elif self.count == 4:
            
            if distance < 0.1:
                rospy.sleep(5.0)
                self.count +=1

        elif self.count == 5:
            if distance < 0.1:

                rospy.sleep(5.0)
                self.count +=1

        elif self.count== 6:
            if distance < 1.0:
                rospy.sleep(5.0)
                self.count +=1

        elif self.count == 7:
            if distance < 1.0:
                rospy.sleep(5.0)
                self.count +=1 

        else:
            if distance < 1.0:
                self.count += 1


        # initial pose update
        if ((self.current_x + 7.4)**2 + (self.current_y - 7.0)**2)**0.5 < 0.5:
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
  
            rospy.sleep(2.0)

        elif ((self.current_x + 2.7)**2 + (self.current_y - 14.75)**2)**0.5 < 0.5:
            self.pose_pub.publish(self.pos)
  
            print("point7")
            rospy.sleep(2.0)

if __name__ =="__main__":
    a = Goal()

