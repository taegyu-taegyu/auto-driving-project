#!/usr/bin/python
from re import T
import rospy
from nav_msgs.msg import OccupancyGrid


M = 75

N = 50

def callback(cmap):
    data = list(cmap.data)
    for y in range(cmap.info.height):
        for x in range(cmap.info.width):
            i = x + (cmap.info.height - 1 - y) * cmap.info.width
            if data[i] >= M:  
                data[i] = 100
            elif (data[i] >= 0) and (data[i] < N):  # free
                data[i] = 0
            else:  
                data[i] = -1
    cmap.data = tuple(data)
    pub.publish(cmap)


rospy.init_node('mapc_node', anonymous=True) 
sub = rospy.Subscriber('/map', OccupancyGrid, callback)
pub = rospy.Publisher('/cmap', OccupancyGrid, queue_size=20)

rospy.spin()