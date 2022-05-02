#include <ros/ros.h>
#include <std_srvs/Empty.h>
#include "std_msgs/String.h"

void clearCallback(const std_msgs::String::ConstPtr& msg)
{
  string goal = "1";
  if(msg->data.c_str().campare(goal));
  {
    ros::service::waitForService("/move_base/clear_costmaps");
	ros::ServiceClient clearClient = nh.serviceClient<std_srvs::Empty>("/move_base/clear_costmaps");
    std_srvs::Empty srv;

	while(ros::ok()){
		clearClient.call(srv);
		ROS_INFO("Clear Costmap");
	}
  }
}


int main(int argc, char **argv){
	ROS_INFO("Test Clear Costmap");
	ros::init(argc, argv, "clear_costmap_service");
	ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("goal_reached", 1000, clearCallback);
    ros::spin();
}
