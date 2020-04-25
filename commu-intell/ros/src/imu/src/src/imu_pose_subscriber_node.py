'''
===============================================================================
imu_pose_subscriber_node.py 
    This program subscribe to the imu publisher node to listen for mpu6050

Author:         Annabel Li, li3317@purdue.edu
Maintainer:     Annabel Li, li3317@purdue.edu
Version:        April 17, 2020
Status:         In progress
===============================================================================
'''

import rospy
from IMU.msg import IMU

def callback(data):
    rospy.loginfo("linear acceleration in x : %.3f , y : %.3f , z : %.3f \ngyroscope acceleration in x : %.3f , y : %.3f , z : %.3f " 
    	% (data.surgin, data.heaving, data.swaying, data.pitch, data.yaw, data.roll))
    
def listener():

    rospy.init_node('imu_raw_data_subscriber')

    rospy.Subscriber("imu_raw_data", IMU, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
