#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped,PoseWithCovarianceStamped ,Twist

class Goal:
    def __init__(self):
        rospy.init_node("Goal")
        # self.goal_position_x = float(input())
        # self.goal_position_y = float(input())
        # self.goal_position_z = float(input())
        self.vel_x = 0
        self.vel_yaw = 0
        self.count = 0
        self.cmd_pub = rospy.Publisher("cmd_vel",Twist,queue_size=1)
        self.pub = rospy.Publisher("/move_base_simple/goal",PoseStamped,queue_size=10)
        rospy.Subscriber("/amcl_pose",PoseWithCovarianceStamped,self.pose_callback)
        rospy.Subscriber("cmd_vel",Twist,self.cmd_vel_callback)
        rospy.Timer(rospy.Duration(1.0),self.callback)
        rospy.spin()
## my pose -> amcl_pose
    def cmd_vel_callback(self,cmd_data):
        self.vel_x = cmd_data.linear.x
        self.vel_yaw = cmd_data.angular.z

    def pose_callback(self, data):

        self.current_x = data.pose.pose.position.x
        self.current_y = data.pose.pose.position.y



    def callback(self,event):
        # print("okay")
        cmd_pub =Twist()
        pub_data = PoseStamped()
        pub_data.header.seq = 1
        pub_data.header.stamp = rospy.Time.now()
        pub_data.header.frame_id = "map"
        pub_data.pose.orientation.x = 0.0
        pub_data.pose.orientation.y =  0.0
        pub_data.pose.orientation.z = -0.75
        pub_data.pose.orientation.w =  0.6675
        goal_xy = [[0.0 , 15.0],[-8.8  ,12.0],[-6.0,-1.5]]
        
        pub_data.pose.position.x = goal_xy[self.count][0]
        pub_data.pose.position.y = goal_xy[self.count][1]
        self.pub.publish(pub_data)
        print("current speed x :{0} z : {1}".format(self.vel_x,self.vel_yaw))
        print("current goal x : {0} y : {1}".format(goal_xy[self.count][0],goal_xy[self.count][1]))
        print("currnt x :{0} y: {1}".format(self.current_x, self.current_y))
        # print("x distance :{0} y distance : {1}".format(abs(self.current_x - goal_xy[self.count][0]),abs(self.current_y - goal_xy[self.count][1])))
        distance = ((self.current_x - goal_xy[self.count][0])**2 +(self.current_y - goal_xy[self.count][1])**2)**0.5
        # if abs(self.current_x - goal_xy[self.count][0]) < 1 and abs(self.current_y - goal_xy[self.count][1]) < 1:
        print("distance = {}".format(distance))
        print("goal number : {}".format(self.count+1))
        print()

        if distance < 0.3:
            # if self.vel_x <= 0.1 and self.vel_yaw < 0.2 :
                self.count +=1
        

  
if __name__ =="__main__":
    a = Goal()

#!/usr/bin/env python
# license removed for brevity

# import rospy

# # Brings in the SimpleActionClient
# import actionlib
# # Brings in the .action file and messages used by the move base action
# from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# def movebase_client():

#    # Create an action client called "move_base" with action definition file "MoveBaseAction"
#     client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
#    # Waits until the action server has started up and started listening for goals.
#     client.wait_for_server()

#    # Creates a new goal with the MoveBaseGoal constructor
#     goal = MoveBaseGoal()
#     goal.target_pose.header.frame_id = "map"
#     goal.target_pose.header.stamp = rospy.Time.now()
#    # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
#     goal.target_pose.pose.position.x = 0.5
#    # No rotation of the mobile base frame w.r.t. map frame
#     goal.target_pose.pose.orientation.w = 1.0

#    # Sends the goal to the action server.
#     client.send_goal(goal)
#    # Waits for the server to finish performing the action.
#     wait = client.wait_for_result()
#    # If the result doesn't arrive, assume the Server is not available
#     if not wait:
#         rospy.logerr("Action server not available!")
#         rospy.signal_shutdown("Action server not available!")
#     else:
#     # Result of executing the action
#         return client.get_result()   

# # If the python node is executed as main process (sourced directly)
# if __name__ == '__main__':
#     try:
#        # Initializes a rospy node to let the SimpleActionClient publish and subscribe
#         rospy.init_node('movebase_client_py')
#         result = movebase_client()
#         if result:
#             rospy.loginfo("Goal execution done!")
#     except rospy.ROSInterruptException:
#         rospy.loginfo("Navigation test finished.")
